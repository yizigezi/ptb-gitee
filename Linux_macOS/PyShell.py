import os

print("PyShell 0.1")
print("On PyDOS")

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