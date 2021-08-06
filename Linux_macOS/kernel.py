import os

print("PyKernel 0.1")
print("On PyDOS")

prompt = "C:\>"

while True:
    command = input(prompt)
    cCode = "python3 " + command + ".py"
    if command == "exit":
        print("Bye")
        break
    else:
        os.system(cCode)
        cCode = "python3 " + command + ".py"