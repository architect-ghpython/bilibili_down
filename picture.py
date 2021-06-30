import requests
import re
from requ import*
import requ
import os
import time
import sys


def download_picture():
    url=input("请输入dynamic_id，比如https://t.bilibili.com/538622902183625245?tab=2输入538622902183625245")
    url=re.findall("\d+", url)
    url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id="+url[0]
    a=htp_1(url)
    b=requ.picture(a)
    print(b[1])

def download_picture2():
    url=input("请输入动态主页")
    url1=re.findall("\d+", url)[0]
    url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid="+url1+"&offset_dynamic_id=0"
    a=requ.circle_picture(url,url1)
    print(requ.lis)
