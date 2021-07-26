import requests
print("PPkg包管理工具 0.1")

print("正在下载pkglist.txt")
url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/pkglist.txt"
headers = {'User-Agent':'OW64; rv:59.0) Chrome/91.0.4472.124'}
myFile = requests.get(url, headers=headers)
open("pkglist.txt" , 'wb').write(myFile.content)
print("下载完成")

with open("pkglist.txt", "r") as f:
    data = f.read().splitlines()

cho = input("请输入要安装的包名：")
num = data.index(cho)
choName = data[num]
url1 = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/"+choName+".py"

myFile = requests.get(url1, headers=headers)
open(choName+".py" , 'wb').write(myFile.content)