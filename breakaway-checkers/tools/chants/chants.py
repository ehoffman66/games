# Arena chants: "Let's go <nickname>!" sung by a crowd of Piper LibriTTS voices, one clip per club, packed into chants.mp3
# with a byte index in chants.json (the same format as calls.mp3). Each voice is pitched and stretched a little differently and
# lands a few milliseconds off the others, then the mix gets an arena's echo. Every clip lasts BEAT*4 seconds of chant so the
# game can clap the "clap clap clap-clap-clap" after it on the beat.
# usage: python3 chants.py MODEL.onnx nicks.json OUTDIR [abbr...]   (MODEL is en-us-libritts-high, a 904-speaker voice)
import sys,os,json,subprocess,random,numpy as np
from piper import PiperVoice, SynthesisConfig
model=sys.argv[1];nicks=json.load(open(sys.argv[2]));out=sys.argv[3];only=sys.argv[4:]
os.makedirs(out,exist_ok=True)
v=PiperVoice.load(model);SR=v.config.sample_rate
# the crowd: ten lower voices and six higher ones, picked from a scan of all 904 speakers for ones that are loud and lively
# (pitch range over 6 semitones), spread evenly across median pitches of 95 to 150 Hz and 185 to 245 Hz
SPK=[90,518,406,627,634,453,663,729,722,159,17,282,93,108,166,611]
BEAT=.5;CH=BEAT*3.6   # the words fill a little less than four beats
def synth(text,spk,seed):
    cfg=SynthesisConfig(speaker_id=spk,length_scale=1.25,noise_scale=.8,noise_w_scale=.95)
    a=np.concatenate([c.audio_float_array for c in v.synthesize(text,syn_config=cfg)])
    idx=np.nonzero(np.abs(a)>.02)[0]
    return a[idx[0]:idx[-1]+1] if len(idx) else a
def ff(a,flt,sr_out=SR):
    pcm=(np.clip(a,-1,1)*32767).astype(np.int16).tobytes()
    r=subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-f","s16le","-ar",str(SR),"-ac","1","-i","-","-af",flt,"-ar",str(sr_out),"-ac","1","-f","s16le","-"],input=pcm,capture_output=True)
    if r.returncode:raise SystemExit(r.stderr.decode())
    return np.frombuffer(r.stdout,np.int16).astype(np.float32)/32767
# the arena: low end and fizz rolled off, a few slap-back echoes off the far end, then squeezed
ROOM="highpass=f=170,lowpass=f=3900,aecho=0.85:0.7:47|89|151|233|340:0.32|0.24|0.17|0.12|0.07,acompressor=threshold=-18dB:ratio=4:attack=5:release=120:makeup=4"
def chant(nick,seed):
    rng=random.Random(seed);text=f"Let's go, {nick}!"
    mix=np.zeros(int(SR*(CH+.6)),np.float32)
    for i,spk in enumerate(SPK):
        a=synth(text,spk,seed+i)
        p=2**(rng.uniform(.6,2.2)/12)            # a touch higher: people shout up
        T=CH*rng.uniform(.97,1.02)
        tempo=(len(a)/SR/p)/T
        b=ff(a,f"asetrate={int(SR*p)},aresample={SR},atempo={max(.5,min(2,tempo)):.4f}")
        b=b/(np.abs(b).max()+1e-6)*rng.uniform(.55,1.0)
        o=int(SR*rng.uniform(0,.035))
        n=min(len(b),len(mix)-o);mix[o:o+n]+=b[:n]
    mix/=np.abs(mix).max()+1e-6
    return ff(mix*.9,ROOM,22050)
def mp3(a):
    pcm=(np.clip(a,-1,1)*32767).astype(np.int16).tobytes()
    r=subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-f","s16le","-ar","22050","-ac","1","-i","-","-c:a","libmp3lame","-b:a","40k","-f","mp3","-"],input=pcm,capture_output=True)
    if r.returncode:raise SystemExit(r.stderr.decode())
    return r.stdout
idx={};blob=bytearray()
for n,(abbr,nick) in enumerate(nicks):
    if only and abbr not in only:continue
    b=mp3(chant(nick,1000+n*37));idx["ch_"+abbr]=[len(blob),len(b)];blob+=b;print(abbr,nick,len(b),flush=True)
open(os.path.join(out,"chants.mp3"),"wb").write(blob);json.dump(idx,open(os.path.join(out,"chants.json"),"w"),separators=(",",":"))
print(len(idx),"chants",len(blob),"bytes","speakers",SPK)
