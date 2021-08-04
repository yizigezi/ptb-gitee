import os

tsf = "C:\>"

zt = "load"

if zt == "load":
    os.system("python BootLoader.py")
    zt = "Running"

command = input(tsf)
while zt == "Running":
    cCode = "python " + command + ".py"
    if command == "exit":
        break
    else:
        os.system(cCode)
        cCode = "python " + command + ".py"
        command = input(tsf)
