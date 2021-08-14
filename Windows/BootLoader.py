import os
import time
import json
# 系统BL程序
with open('settings.json','r') as s:
    settings = json.load(s)
print("BootLoader running....done")
time.sleep(1)
if settings["Boot Info"] == "True":
    os.system("python.exe sysver.py")
    print("若您不想看见启动信息，可以修改setting.json的Boot Info为False")

print("System Staring....")
print("Welcome to PyDos")
print()
print()
print()
os.system("python.exe kernel.py")
