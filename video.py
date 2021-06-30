import requests
import re
from requ import*
import requ
import os
import time
import sys
def download_video():
    url=input("请输入url")
    b=requ.video(htp_1(url))
    audio=requ.get_video(b[1],url,b[2],".mp3")
    video=requ.get_video(b[0],url,b[2],".mp4")
    cmd="ffmpeg -i  "+b[2]+".mp3  " +"  -i " +b[2]+".mp4  "+  "-c:v copy -c:a aac -strict experimental "+"video\\"+b[2]+".mp4"

    os.system(cmd)

    os.remove(b[2]+".mp3")

    os.remove(b[2]+".mp4")



"""
a=open(b[2]+"1.mp4","wb")
a.write(audio)
a.close()

a=open(b[2]+".mp4","wb")
a.write(video)
a.close()
"""