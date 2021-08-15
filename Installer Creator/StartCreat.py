import requests

print("开始部署")
url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/installer-creator/config.py"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
filename = "config.py"
for i in range(2):
    with open(filename, "wb") as f:
        myfile = requests.get(url, headers=headers)
        f.write(myfile.content)
    url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/installer-creator/installer.py"
    filename = "installer.py"

urlb = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/installer-creator/build.bat"
with open("build.bat", "wb") as b:
    build = requests.get(urlb, headers=headers)
    b.write(build.content)
print("部署完成，请修改config.py以自定义您的安装程序")
