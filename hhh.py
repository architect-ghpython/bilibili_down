import video
import picture
while True:
    aa=input("请输入：1视频2图片3评论")
    if aa=="1":

        video.download_video()
    if aa=="2":
        tu=input("模式：1所有2指定动态")
        if tu=="2":
            picture.download_picture()
        if tu =="1":
            picture.download_picture2()

     
        