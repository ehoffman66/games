# append newly generated clips (gen.py output for just the new ids) onto an existing calls.mp3 + calls.json
# usage: python3 merge.py BASE_DIR NEW_DIR OUT_DIR
import sys,json,os
base,new,out=sys.argv[1:4];os.makedirs(out,exist_ok=True)
bi=json.load(open(base+"/calls.json"));bb=open(base+"/calls.mp3","rb").read()
ni=json.load(open(new+"/calls.json"));nb=open(new+"/calls.mp3","rb").read()
blob=bytearray(bb);idx=dict(bi)
for k,(o,n) in ni.items():
    if k in idx:print("replacing",k)
    idx[k]=[len(blob),n];blob+=nb[o:o+n]
open(out+"/calls.mp3","wb").write(blob);json.dump(idx,open(out+"/calls.json","w"),separators=(",",":"))
print(len(idx),"clips",len(blob),"bytes")
