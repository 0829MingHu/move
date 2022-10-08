import os
import shutil

num=0
rootpath=r"home\chenj0g\rgb_flow\rgb"
dirpath=r"home\chenj0g\rgb_flow"
for curdir,roots,files in os.walk(rootpath):
    num=num+1
N=4
num=(num-1)/4
print(num)
dirend=['rgb1','rgb2','rgb3','rgb4']
cnt=0
flag=0
for curdir,roots,files in os.walk(rootpath):
    if cnt==0:
        cnt=1
        continue
    if cnt>num:
        cnt=1
        flag=flag+1
    tp=dirend[flag]
    d1=curdir.split('\\')[-1]
    savename=tp+'/'+d1
    cnt=cnt+1
    print(savename)
    # shutil.move(curdir,filename)

