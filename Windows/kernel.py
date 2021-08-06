import os

prompt = "C:\>"

while True:
command = input(prompt)
    cCode = "python.exe " + command + ".py"
    if command == "exit":
        break
    else:
        os.system(cCode)
        cCode = "python.exe " + command + ".py"