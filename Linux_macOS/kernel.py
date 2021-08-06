import os

print("PyKernel 2.0 Cheetah")
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