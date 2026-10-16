# Build the announcer clips with Piper: one small MP3 per call, packed end to end into calls.mp3 with a byte index in calls.json.
# usage: python3 gen.py MODEL.onnx SPEAKER_ID OUTDIR [ids...]   (speaker -1 for single-voice models)
import sys,os,io,json,wave,subprocess,numpy as np
from piper import PiperVoice, SynthesisConfig
from script import script
model,spk,out=sys.argv[1],int(sys.argv[2]),sys.argv[3];only=sys.argv[4:]
os.makedirs(out,exist_ok=True)
v=PiperVoice.load(model);SR=v.config.sample_rate
S=script()
# broadcast-booth polish: trim the rumble and hiss, even out the level, a short touch of room
FX="highpass=f=90,lowpass=f=8500,acompressor=threshold=-21dB:ratio=3:attack=4:release=80:makeup=3,aecho=0.7:0.6:28|55:0.10|0.05"
# excited calls: a semitone and a half higher at the same speed
EXC="asetrate=%d,aresample=%d,atempo=%.4f,"%(int(SR*1.09),SR,1/1.09)
def synth(text,style):
    ls={"x":.82,"n":.9,"l":.95}.get(style,.88)
    cfg=SynthesisConfig(speaker_id=None if spk<0 else spk,length_scale=ls,noise_scale=.75 if style=="x" else .667,noise_w_scale=.9)
    a=np.concatenate([c.audio_float_array for c in v.synthesize(text,syn_config=cfg)])
    # trim the silence Piper leaves around a line (keep 30 ms)
    idx=np.nonzero(np.abs(a)>.02)[0];pad=int(.03*SR)
    if len(idx):a=a[max(0,idx[0]-pad):idx[-1]+pad]
    return a
def mp3(a,style):
    pcm=(np.clip(a,-1,1)*32767).astype(np.int16).tobytes()
    flt=(EXC if style=="x" else "")+FX
    r=subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-f","s16le","-ar",str(SR),"-ac","1","-i","-","-af",flt,"-ar","22050","-ac","1","-c:a","libmp3lame","-b:a","40k","-f","mp3","-"],input=pcm,capture_output=True)
    if r.returncode:raise SystemExit(r.stderr.decode())
    return r.stdout
idx={};blob=bytearray()
for k,(t,st) in S.items():
    if only and k not in only:continue
    b=mp3(synth(t,st),st);idx[k]=[len(blob),len(b)];blob+=b
open(os.path.join(out,"calls.mp3"),"wb").write(blob);json.dump(idx,open(os.path.join(out,"calls.json"),"w"),separators=(",",":"))
print(len(idx),"clips",len(blob),"bytes")
