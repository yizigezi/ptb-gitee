# Installer Creator

name = "py-dos"

installer_name = "py-dos installer by yizigezi"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

url = "https://pydos-1301360149.cos.ap-nanjing.myqcloud.com/py-dos-win.zip"

filename = "py-dos-win.zip"

boot_filedir = '\\py-dos-win\\InstallPkg.bat'   # 可选，安装后要启动的文件

command = 'python '      # 可选，如需要安装后启动python文件，可填入"python "或"python3 "（注意空格）,bat文件则不填此项

ourl = 'https://gitee.com/yizhigezi_yijiafeiji/py-dos/tree/master'   # 安装完成后要打开的页面（最好是帮助页面或官方网站）