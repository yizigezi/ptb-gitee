import os

tsf = "C:\>"

while True:
    command = input(tsf)
    cCode = "python3 " + command + ".py"
    if command == "exit":
        print("Bye")
        break
    else:
        os.system(cCode)
        cCode = "python3 " + command + ".py"