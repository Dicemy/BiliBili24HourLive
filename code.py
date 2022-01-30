import os
import os.path
import io

dir = input("请输入视频所在地址:\n")
rtmp = input("请输入B站直播串流密钥:\n")
nameList = []

def listDir(dirTemp):
    global nameList
    if not os.path.exists(dirTemp):
        print ("file or directory isn't exist")
        return
    if os.path.isfile(dirTemp):
        nameList.append(dirTemp)
        return
    resultList = os.listdir(dirTemp)
    for fileOrDir in resultList:
        listDir(dirTemp + "/" +fileOrDir)
    return nameList

def main():
    while True:
        List = listDir(dir)
        List.sort()
        for file in List:
            print(file)
            fw = io.open("mylog", 'a+', encoding='utf8')
            fw.write(file)
            fw.write('\n')
            tmpint = file.rfind('/')
            filename = file[tmpint:]
            os.system('ffmpeg -re -i "' + file + '"  -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://live-push.bilivideo.com/live-bvc/' + rtmp + '"')
main()
