import os,sys,random as r
def s(f):
    with open(f,'wb') as x:x.write(b'\x00'*os.path.getsize(f)+b'\xFF'*os.path.getsize(f)+bytes([r.randint(0,255)for _ in range(os.path.getsize(f))]))
    os.remove(f)
sys.exit(print(f"Usage: secdel {{file_to_delete}}")) if len(sys.argv) != 2 else (s(sys.argv[1]), print(f"File {sys.argv[1]} has been deleted"))