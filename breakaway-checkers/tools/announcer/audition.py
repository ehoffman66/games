# one short play-by-play sequence per candidate voice, as an MP3 Erik can play on his phone
import sys,os,subprocess,json
seq=["c_welcome","t_full_CLT","c_versus","t_full_HER","c_herecomes","n_NOVAK","m_toedrag","g_whatamove","g_cookies","t_goal_CLT","c_upnext","num_17","s_poke1","s_whatastop","e_thatsit","t_win_CLT"]
out=sys.argv[1];os.makedirs(out,exist_ok=True)
for name,model,spk in [tuple(x.split(":")) for x in sys.argv[2:]]:
    d=os.path.join(out,"_"+name);subprocess.run(["python3","gen.py",model,spk,d,*seq],check=True)
    idx=json.load(open(d+"/calls.json"));blob=open(d+"/calls.mp3","rb").read()
    parts=[]
    for i,k in enumerate(seq):
        p=f"{d}/{i:02d}.mp3";open(p,"wb").write(blob[idx[k][0]:idx[k][0]+idx[k][1]]);parts.append(p)
    # the way the game plays them: back to back with a short breath (a longer one between calls)
    gaps={3:.5,5:.15,6:.35,9:.6,11:.2,13:.6};inputs=[];fl=[]
    for i,p in enumerate(parts):
        inputs+=["-i",p];fl.append(f"[{i}:a]apad=pad_dur={gaps.get(i,.08)}[a{i}]")
    fl.append("".join(f"[a{i}]" for i in range(len(parts)))+f"concat=n={len(parts)}:v=0:a=1[o]")
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error",*inputs,"-filter_complex",";".join(fl),"-map","[o]","-c:a","libmp3lame","-b:a","64k",f"{out}/{name}.mp3"],check=True)
    print(name,os.path.getsize(f"{out}/{name}.mp3"))
