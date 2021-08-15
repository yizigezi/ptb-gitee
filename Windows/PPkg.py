import os
import requests
import json

print("PPkg Package Manager 0.1")

# 系统识别\head获取
with open("settings.json", "r") as s:
    sets = json.load(s)
    head = sets["User Agent"]
    system = sets["system"]

headers = {
    'User-Agent': head
}


def uplist():
    print("Downloading pkglist.txt")
    url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/pkglist.txt"
    myFile = requests.get(url, headers=headers)
    open("pkglist.txt", 'wb').write(myFile.content)
    print("Download done")


def file_name(file_dir):
    global files
    for root, dirs, files in os.walk(file_dir):
        # 当前路径下所有非目录子文件
        print(files)
    return files


def install():
    with open("pkglist.txt", "r") as f:
        data = f.read().splitlines()
    choi = input("install>")
    num = data.index(choi)
    choName = data[num]
    url1 = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/" + system + "/" + choName + ".py"
    myFile = requests.get(url1, headers=headers)
    open(choName + ".py", 'wb').write(myFile.content)


def remove():
    cmr = input("remove>")
    upkg = cmr + ".py"
    confirm = input("确认删除？(Y/n)")
    if confirm == "Y":
        ccm = "del " + upkg
        os.system(ccm)
    elif confirm == "n":
        pass


def updatesys():
    url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/update.exe"
    myFile = requests.get(url, headers=headers)
    open("./update.exe", 'wb').write(myFile.content)
    os.system("update.exe")


def reset():
    url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/" + system + "/settings.json"
    res = requests.get(url, headers=headers)
    open("settings.json", "wb").write(res.content)
    print("done")


print("install:安装包   remove:删除包    updata:更新pkglist.txt    updatesys:更新软件   reset:恢复原始设置（从腾讯云下载settings.json）")
cm = input("请选择操作:")

if cm == "install":
    install()
elif cm == "remove":
    remove()
elif cm == "updata":
    uplist()
elif cm == "updatesys":
    updatesys()
elif cm == "reset":
    r = input("确认恢复原始设置？(Y/n)")
    if r == "Y":
        reset()
    else:
        pass
