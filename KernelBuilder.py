import webbrowser,sys,subprocess
import math
import pyperclip
import os
import time

address=0x4000000
code=""
offset=0

popen = subprocess.Popen('assemble\\build.bat',shell=True)
popen.wait()

with open("assemble\\asm",'rb') as f:
    tmp=f.read()
    f.close()
tmp=tmp.hex().upper()

time.sleep(0.5)

s=[]
for x in range(math.floor(len(tmp)/8)):
    s.append(tmp[x*8:x*8+8])
    
for x in range(len(s)):
    code=code+(format(address+offset,'08X')+" "+s[x][0:8])+"\n"
    offset=offset+4
    
time.sleep(0.5)

code=code[:-1]

pyperclip.copy(code)
print("Copied to clipboard!")
time.sleep(3)
