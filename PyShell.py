import os

tsf = "PyDOS\>"

zt = "load"

if zt == "load":
    os.system("python.exe BootLoader.py")
    zt = "Running"

command = input(tsf)
while zt == "Running":
    cCode = "python.exe " + command + ".py"
    if command == "exit":
        print("请再输入以确认。")
        break
    else:
        os.system(cCode)
        cCode = "python.exe " + command + ".py"
        command = input(tsf)