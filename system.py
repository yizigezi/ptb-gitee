import os

tsf = "C\>"

zt = "load"

if zt == "load":
    os.system("python.exe BootLoader.py")
    zt = "Running"

command = input(tsf)
# PyShell
while zt == "Running":
    if command == "sys.ver":
        os.system("python.exe sysver.py")

    elif command == "calcutator":
        os.system("python.exe Calcutator.py")

    elif command == "ASCII":
        os.system("python.exe ASCII.py")

    elif command == "adb":
        os.system("adb.exe")

    elif command == "help":
        os.system("python.exe help.py")
    elif command == "Note":
        os.system("python.exe notepad.py")
    elif command == "update--system":
        os.system("python.exe update.py")
    elif command == "Rename":
        os.system("python.exe PyRename.py")
    elif command == "Music":
        os.system("python.exe PyMusic.py")
    elif command == "PPkg":
        os.system("python.exe PPkg.py")
    elif command == "exit":
        print("请再输入以确认。")
        break
    else:
        os.system(command)

    command = input(tsf)
