import os
import shutil

num=0
rootpath=r"/home/chenj0g/rgb_flow/queshi"
for curdir,roots,files in os.walk(rootpath):
    for file in files:
        num=num+1
N=4
print(num)
num=int(num/N)
print(num)
cnt=0
dirpath=r"/home/chenj0g/rgb_flow"
dirend=['rgbflow_queshi1','rgbflow_queshi2','rgbflow_queshi3','rgbflow_queshi4']
flag=0
for curdir,roots,files in os.walk(rootpath):
    for file in files:

        if cnt-num>=0 and not flag==N-1:
            cnt=cnt-num
            flag=flag+1
        if not os.path.exists(dirpath+dirend[flag]):
            os.mkdir(dirpath+dirend[flag])
        savename=dirpath+dirend[flag]+'/'+file
        print(savename)
        shutil.move(curdir+'/'+file,savename)
        cnt = cnt + 1
