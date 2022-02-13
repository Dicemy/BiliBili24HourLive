import os
import os.path
import io

dir = input("请输入视频所在文件夹地址（或者文件地址）:\n")
rtmp = input("请输入B站直播串流密钥:\n")
fps = input("请输入要进行推流的帧率:\n")

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
    #     用递归将文件目录中的文件全部加入到nameList中
    return nameList

def getfilename(file):
    tmpint = file.rfind('/')
    filename = file[tmpint + 1:]
    return filename


def main():
    while True:
        List = listDir(dir)
        List.sort()
        for file in List:
            print(file)
            fw = io.open("mylog", 'a+', encoding='utf8')
            fw.write(file)
            fw.write('\n')
            filename = getfilename(file)
            os.system('ffmpeg -re -i "' + file + '" -vcodec libx264 -acodec copy -b:a 192k -r ' + fps + ' -vf "drawtext=fontsize=24:fontfile=FreeSerif.ttf:text=\'' + filename + '\':x=10:y=main_h-30:fontcolor=LightGrey:alpha=0.6" -f flv "rtmp://live-push.bilivideo.com/live-bvc/' + rtmp + '"')
main()