import os

repo = " -i https://pypi.tuna.tsinghua.edu.cn/simple"
pkglist = "requests pygame pillow pymediainfo pycryptodome psutil"
os.system("pip install " + pkglist + repo)