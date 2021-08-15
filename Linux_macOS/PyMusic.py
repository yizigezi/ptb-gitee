import base64  # download库
import binascii
import json
import string
from urllib import parse

# player库
import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Scale
from tkinter import Label
from PIL import Image, ImageTk
from tkinter import Toplevel
from pymediainfo import MediaInfo
import re
from tkinter import Message
import threading
import pygame
import time
import os
import random
from tkinter.filedialog import askopenfilename
from tkinter import StringVar

with open("settings.json", "r") as s:
    sets = json.load(s)
    head = sets["User Agent"]

def download():
    import requests
    from Crypto.Cipher import AES

    # 初始化数据 (list)

    urlList = []
    songNames = []

    print("PyMusic Download组件  0.0.1")

    def get_random():
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        return random_str

    def len_change(text):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        text = text.encode("utf-8")
        return text

    def aes(text, key):
        iv = b'0102030405060708'
        text = len_change(text)
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(text)
        encrypt = base64.b64encode(encrypted).decode()
        return encrypt

    def b(text, str):
        first_data = aes(text, '0CoJUm6Qyw8W8jud')
        second_data = aes(first_data, str)
        return second_data

    def c(text):
        e = '010001'
        f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        text = text[::-1]
        result = pow(int(binascii.hexlify(text.encode()), 16), int(e, 16), int(f, 16))
        return format(result, 'x').zfill(131)

    def get_final_param(text, str):
        params = b(text, str)
        encSecKey = c(str)
        return {'params': params, 'encSecKey': encSecKey}

    def get_music_list(params, encSecKey):
        url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="

        payload = 'params=' + parse.quote(params) + '&encSecKey=' + parse.quote(encSecKey)
        headers = {
            'authority': 'music.163.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'origin': 'https://music.163.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://music.163.com/search/',
            'accept-language': 'zh-CN,zh;q=0.9',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    def get_reply(params, encSecKey):
        url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
        payload = 'params=' + parse.quote(params) + '&encSecKey=' + parse.quote(encSecKey)
        headers = {
            'authority': 'music.163.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'origin': 'https://music.163.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://music.163.com/',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    if __name__ == '__main__':
        song_name = input('请输入歌曲名称，按回车键搜索：')
        d = {"hlpretag": "<span class=\"s-fc7\">", "hlposttag": "</span>", "s": song_name, "type": "1", "offset": "0",
             "total": "true", "limit": "30", "csrf_token": ""}
        d = json.dumps(d)
        random_param = get_random()
        param = get_final_param(d, random_param)
        song_list = get_music_list(param['params'], param['encSecKey'])
        print('搜索结果如下：')
        if len(song_list) > 0:
            song_list = json.loads(song_list)['result']['songs']
            for i, item in enumerate(song_list):
                item = json.dumps(item)
                songNamed = str(i) + "：" + json.loads(str(item))['name']
                songNames.append(songNamed)
                d = {"ids": "[" + str(json.loads(str(item))['id']) + "]", "level": "standard", "encodeType": "",
                     "csrf_token": ""}
                d = json.dumps(d)
                param = get_final_param(d, random_param)
                song_info = get_reply(param['params'], param['encSecKey'])
                if len(song_info) > 0:
                    song_info = json.loads(song_info)
                    song_url = json.dumps(song_info['data'][0]['url'], ensure_ascii=False)
                    song_url = eval(song_url)
                    urlList.append(song_url)
                else:
                    print("该首歌曲解析失败，可能是因为歌曲格式问题")
        else:
            print("很抱歉，未能搜索到相关歌曲信息")

    cho = int(input("请输入歌曲序号"))
    url = urlList[cho]
    headers = {
        'User-Agent': head
               }
    myfile = requests.get(url, headers=headers)
    open("./Download/" + songNames[cho] + ".mp3", 'wb').write(myfile.content)


print("PyMusic Player组件 0.0.1 Beta")
top = tkinter.Tk()
top.geometry("800x400")
top.title("PyMusic Player")


def printsrceen(texts):
    t = int(texts)
    top.attributes("-alpha", t / 100)


screenwidth = top.winfo_screenwidth()
screenheight = top.winfo_screenheight() - 100

pygame.init()
path = StringVar()
paths = StringVar()
patht = StringVar()
v = StringVar()
v1 = StringVar()
file_dir = ".\Download"


def callback():
    path_ = askopenfilename()
    return path_


musicPath = os.path.abspath(os.path.dirname(__file__))


def selectPath():
    def file_name(file_dir):
        global files
        for root, dirs, files in os.walk(file_dir):
            # 当前路径下所有非目录子文件
            print(files)
        return files

    fil = file_name(file_dir)
    count = len(file_name(file_dir))

    s = random.randint(0, count - 1)
    fil2 = file_dir + "\\" + fil[s]
    pygame.mixer.music.load(fil2)
    pygame.mixer.music.play(1, 0)
    media_info = MediaInfo.parse(fil2)
    data = media_info.to_json()
    rst = re.search('other_duration.*?(.*?)min(.*?)s.*?', data)
    t = int(rst.group(0)[19:20])
    r = int(rst.group(0)[-4:-2])
    m = (t * 60 + r) * 1000

    musictime = str(t) + ':' + str(r)
    l2.config(text=fil2)
    l3.config(text=musictime)
    lbTime = tkinter.Label(top, anchor='w')
    lbTime.place(x=25, y=150)


def printScale(text):
    t = int(text)
    pygame.mixer.music.set_volume(t / 100)


def update_timeText():
    current = time.strftime("%H:%M:%S")

    timeText.configure(text=current)

    top.after(1000, update_timeText)


def remind():
    top = Toplevel()
    top.title('使用提示')
    top.geometry("200x200")
    t = "半分钟后开始播放音乐"
    msg = Message(top, text=t)
    msg.config(font=('times', 18, 'italic'))
    msg.place(x=0, y=0)
    lbTime = tkinter.Label(top, fg="red", anchor='w')
    lbTime.place(x=100, y=45)

    def autoclose():
        for i in range(30):
            lbTime['text'] = '距离窗口关闭还有{}秒'.format(30 - i)
            time.sleep(1)
        top.destroy()

    t = threading.Thread(target=autoclose)
    t.start()
    loopl = top.after(60 * 59500, remind)


def play():
    f = callback()
    pygame.mixer.music.load(f)
    pygame.mixer.music.play()
    path.set(f)
    media_info = MediaInfo.parse(f)
    data = media_info.to_json()
    rst = re.search('other_duration.*?(.*?)min(.*?)s.*?', data)
    t = int(rst.group(0)[19:20])
    r = int(rst.group(0)[-4:-2])
    m = (t * 60 + r) * 1000
    musictime = str(t) + ':' + str(r)
    l2.config(text=f)
    l3.config(text=musictime)
    lbTime = tkinter.Label(top, anchor='w')
    lbTime.place(x=25, y=150)

    def autoclose():
        for i in range(m // 1000):
            lbTime['text'] = '-{} /'.format((m // 1000) - i)
            time.sleep(1)

    t = threading.Thread(target=autoclose)
    t.start()
    loopl = top.after(m, selectPath)


def stop(loopl):
    pygame.mixer.music.stop()
    top.after_cancel(loopl)


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def choosepic():
    path_s = askopenfilename()
    paths.set(path_s)
    img_open = Image.open(e1.get())
    img = ImageTk.PhotoImage(img_open)
    l1.config(image=img)
    l1.image = img


def loops():
    selectPath()


def gettime():
    t = time.strftime('%H%M%S')
    s = int(t[0:2])
    d = int(t[2:4])
    f = int(t[4:6])
    g = s * 60 * 60 + d * 60 + f
    return g


def opendownload():
    download()


errmsg = 'Error!'
timeText = Label(top, text="", font=("Helvetica", 15))
timeText.place(x=180, y=370)
update_timeText()
Button(top, text="选择文件/播放", command=play, width=10, bg="sky blue").place(x=20, y=20)
Entry(top, text=path, width=25, state='readonly').place(x=120, y=20)

Button(top, text='选择图片', command=choosepic, width=10, bg="sky blue").place(x=20, y=55)
e1 = Entry(top, text=paths, state='readonly', width=25)
e1.place(x=120, y=55)
l1 = Label(top)
l1.place(x=320, y=0)

Button(top, text="随机播放", command=selectPath, width=7, bg="sky blue").place(x=20, y=225)
l2 = Label(top, text='', width=25, font=("Helvetica", 16))
l2.place(x=0, y=100)
Button(top, text="下一首", command=loops, width=5, bg="sky blue").place(x=100, y=225)
l3 = Label(top, text='', width=15)
l3.place(x=24, y=150)

Button(top, text="暂停", command=pause, width=7, bg="sky blue").place(x=170, y=245)
Button(top, text="继续播放", command=unpause, width=7, bg="sky blue").place(x=170, y=205)
Button(top, text="结束播放", command=stop, width=7, bg="sky blue").place(x=240, y=205)
Button(top, text="下载歌曲", command=download, width=7, bg="sky blue").place(x=240, y=245)

w1 = Scale(top, from_=0, to=100, orient="horizontal", length=75, variable=v, command=printScale, label="音量")
w1.place(x=240, y=145)

top.mainloop()
