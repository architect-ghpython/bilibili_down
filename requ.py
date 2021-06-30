import requests
import re
import json
import os
import time
import sys 
def htp_1(url):
    headers = {
    
"authority":	"cn-sdjn2-cmcc-v-04.bilivideo.com",
"path":	"/upgcxcode/68/22/345232268/345232268-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1625046487&gen=playurlv2&os=vcache&oi=3748145769&trid=0001a79668ea65e84e029c0a0065d12a6e3au&platform=pc&upsig=a06305d0f71c00c6a71db8ccc0a02164&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=4053&mid=1522826701&bvc=vod&orderid=1,3&agrr=1&logo=40000000",
"pragma":	"no-cache",
"cache-control":	"no-cache",
"sec-ch-ua":	"\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
"sec-ch-ua-mobile":	"?0",
"user-agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
"accept":	"*/*",
"origin":	"https://www.bilibili.com",
"sec-fetch-site":	"cross-site",
"sec-fetch-mode":	"cors",
"sec-fetch-dest":	"empty",
"referer":	url,
"accept-encoding":	"identity",
"accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,v=b3",
     'accept-Encoding': "gzip, deflate"
    
    
    } 
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    text=response.text
    return text
def htp_2(url,url2,name,typ):
    headers = {
    
"authority":	"cn-sdjn2-cmcc-v-04.bilivideo.com",
"path":	"/upgcxcode/68/22/345232268/345232268-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1625046487&gen=playurlv2&os=vcache&oi=3748145769&trid=0001a79668ea65e84e029c0a0065d12a6e3au&platform=pc&upsig=a06305d0f71c00c6a71db8ccc0a02164&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=4053&mid=1522826701&bvc=vod&orderid=1,3&agrr=1&logo=40000000",
"pragma":	"no-cache",
"cache-control":	"no-cache",
"sec-ch-ua":	"\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
"sec-ch-ua-mobile":	"?0",
"user-agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
"accept":	"*/*",
"origin":	"https://www.bilibili.com",
"sec-fetch-site":	"cross-site",
"sec-fetch-mode":	"cors",
"sec-fetch-dest":	"empty",
"referer":	url2,
"accept-encoding":	"identity",
"accept-language": "zh-CN,zh;q=0.9,en;q=0.8"   
    } 
    basename=name+typ
    file_name = os.getcwd() + '/'+basename
    if not os.path.exists("video"):
      os.makedirs("video")
    start = time.time()
    temp_size = 0 
    chunk_size = 1024
    res = requests.get(url,headers=headers)
    total_size = int(res.headers.get("Content-Length"))
    if res.status_code ==200:
        print('[文件大小]:%0.2f MB' %(total_size / chunk_size /1024)) #换算单位并打印
                    #保存下载文件
        with open(file_name, 'wb') as f:
            for chunk in res.iter_content(chunk_size=chunk_size):
                if chunk:
                    temp_size += len(chunk)
                    f.write(chunk)
                    f.flush()
                                #############花哨的下载进度部分###############
                    done = int(50 * temp_size / total_size)
                                # 调用标准输出刷新命令行，看到\r 回车符了吧
                                # 相当于把每一行重新刷新一遍
                    sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                    sys.stdout.flush()
        print()  # 避免上面\r 回车符，执行完后需要换行了，不然都在一行显示
        end = time.time() #结束时间
        print('全部下载完成!用时%.2f 秒' %(end-start))
    else:
        print(res.status_code)

def htp_3(url):
    headers = {
    
"authority":	"cn-sdjn2-cmcc-v-04.bilivideo.com",
"path":	"/upgcxcode/68/22/345232268/345232268-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1625046487&gen=playurlv2&os=vcache&oi=3748145769&trid=0001a79668ea65e84e029c0a0065d12a6e3au&platform=pc&upsig=a06305d0f71c00c6a71db8ccc0a02164&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=4053&mid=1522826701&bvc=vod&orderid=1,3&agrr=1&logo=40000000",
"pragma":	"no-cache",
"cache-control":	"no-cache",
"sec-ch-ua":	"\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
"sec-ch-ua-mobile":	"?0",
"user-agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
"accept":	"*/*",
"origin":	"https://www.bilibili.com",
"sec-fetch-site":	"cross-site",
"sec-fetch-mode":	"cors",
"sec-fetch-dest":	"empty",
"referer":	url,
"accept-encoding":	"identity",
"accept-language": "zh-CN,zh;q=0.9,en;q=0.8"

    
    
    } 
    response = requests.get(url,headers=headers)
    text=response.content
    return text

def video(text):
    import re
    text1=re.findall("window.__playinfo__=(.*)</script><script>window.__INITIAL_STATE__=",text)[0]
    text2=re.findall("data-vue-meta=\"true\">(.*)_哔哩哔哩_bilibili</title>",text)[0]
    #print(text1)
    j = json.loads(text1)
    data1=j["data"]
    data2=data1.get("dash")
    data3=data2.get("video")
    data4=data3[1]
    video=data4.get("baseUrl")
    audio=data2.get("audio")[0]
    audio=audio.get("baseUrl")

    #urls=re.findall("baseUrl\":(.*)\"base_url\"",text1[0])
    return video,audio,text2

def get_video(video,url2,name,typ):
    return  htp_2(video,url2,name,typ)
     
def picture(text):
    import re
    user=re.findall("uname\":\"(.*)\",\"face",text)[0]
    print(user)
    text1=re.findall("face\":\"(.*)\"},\"card\":{\"off",text)[0]
    print(text1)
    j = json.loads(text)
    text2=j["data"]
    text2=text2.get("card")
    text2=text2.get("card")
    text2=re.findall("pictures(.*)pictures_count",text2)[0]
    text2=text2.split(",")

    print(text2[0])
    if not os.path.exists(user):
      os.makedirs(user)
    a=open(user+"\\"+user+".png","wb")
    a.write(htp_3(text1))
    a.close()
    b=1
    time2=time.time()
    for i in text2:
        if "http" in i:
            i=i.replace("\\","")
            i=i.replace("\"","")
            i=i.replace("img_src:","")

            a=open(user+"\\"+str(time2)+"_"+str(b)+".png","wb")
            a.write(htp_3(i))
            a.close()
            print("第{0}张图片下载成功".format(b))
            b+=1
    print("下载完毕")

    return text1,text2

lis=[]
user_=["1"]
user_p=["1"]
def circle_picture(url,url1):
    text=htp_1(url)

    if user_[0]=="1":
         aaa=re.findall("uname\":\"(.*)\",\"face",text)[0]
         user_[0]=aaa.split(",")[0]
         user_[0]=user_[0].replace("\"","")
         user_p[0]=aaa.split(",")[1]
         user_p[0]=user_p[0].replace("\"","")
         user_p[0]=user_p[0].replace("}","")
         user_p[0]=user_p[0].replace("face:","")
         if not os.path.exists(user_[0]):
            os.makedirs(user_[0])
            a=open(user_[0]+"\\"+user_[0]+".png","wb")
            a.write(htp_3(user_p[0]))
            a.close()
         if not os.path.exists(user_[0]+"_all"):
            os.makedirs(user_[0]+"_all")



  
    j = json.loads(text)
    text2=j["data"]
    text2=text2.get("cards")
    for i in text2:
        text3=i.get("card")
        lis.append(text3)
    dynamic_id=((text2[-1]).get("desc")).get("dynamic_id")
    print(dynamic_id)
    url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid="+url1+"&offset_dynamic_id="+str(dynamic_id)
    text=htp_1(url)
    j = json.loads(text)
    text2=j["data"]
    text2=text2.get("cards")
    try:
        dynamic_id2=((text2[-1]).get("desc")).get("dynamic_id")
    except:
        time2=time.time()
        dynamic_id2=0
        img_url=[]
        for i in lis:
            text2=i.split(",")
            for j in text2:
                if "img_src" in j:
                    ii=j.replace("\\","")
                    ii=ii.replace("\"","")
                    ii=ii.replace("img_src:","")
                    img_url.append(ii)
        bb=1
        user=user_[0]
        for i in img_url:  
            a=open(user+"_all"+"\\"+str(time2)+"_"+str(bb)+".png","wb")
            a.write(htp_3(i))
            a.close()
            print("第{0}张图片下载成功".format(bb))
            bb+=1
        print("下载完毕")
        return
    if dynamic_id==dynamic_id2:
        return
    else :
        for i in text2:
            text3=i.get("card")
            lis.append(text3)    
        circle_picture(url,url1)


