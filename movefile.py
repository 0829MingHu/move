import os
import shutil

num=0
rootpath=r"/home/chenj0g/rgb_flow/queshi"
dirpath=r"/home/chenj0g/rgb_flow"
for curdir,roots,files in os.walk(rootpath):
    print(curdir)
    num=num+1
N=4
num=(num)/4
num=max(1,num)
print(num)
dirend=['/home/chenj0g/rgb_flow/rgbflow_queshi1','/home/chenj0g/rgb_flow/rgbflow_queshi2','/home/chenj0g/rgb_flow/rgbflow_queshi3','/home/chenj0g/rgb_flow/rgbflow_queshi4']
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
    d1=curdir.split('/')[-1]
    savename=tp+'/'+d1
    cnt=cnt+1
    print(savename)
    # shutil.move(curdir,savename)

