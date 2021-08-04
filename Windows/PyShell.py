import os

tsf = "C:\>"

zt = "load"

if zt == "load":
    os.system("python.exe BootLoader.py")
    zt = "Running"

command = input(tsf)
while zt == "Running":
    cCode = "python.exe " + command + ".py"
    if command == "exit":
        break
    else:
        os.system(cCode)
        cCode = "python.exe " + command + ".py"
        command = input(tsf)