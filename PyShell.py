import os

tsf = "C:\>"

zt = "load"

command = input(tsf)
while True:
    cCode = "python3 " + command + ".py"
    if command == "exit":
        break
    else:
        os.system(cCode)
        cCode = "python3 " + command + ".py"
        command = input(tsf)
