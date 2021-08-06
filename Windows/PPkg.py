import os
import sys
import requests

print("PPkg Package Manager 0.1")

headers = {'User-Agent': 
            'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
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
    url1 = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/Windows/" + choName + ".py"
    myFile = requests.get(url1, headers=headers)
    open(choName + ".py", 'wb').write(myFile.content)

def remove():
    cmr = input("remove>")
    upkg = cmr + ".py"
    confirm = input("确认删除？ [Y]是  [N]取消")
    if confirm == "Y":
        ccm = "del " + upkg
        os.system(ccm)
    elif confirm == "N":
        sys.exit(0)

def updatesys():
    url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/Windows/update.exe"
    myFile = requests.get(url, headers=headers)
    open("./update.exe" , 'wb').write(myFile.content)
    os.system("update.exe")

print("install:安装包   remove:删除包    updata:更新pkglist.txt    updatesys:更新软件")
cm = input("请选择操作:")

if cm == "install":
    install()
elif cm == "remove":
    remove()
elif cm == "updata":
    uplist()
elif cm == "updatesys":
    updatesys()