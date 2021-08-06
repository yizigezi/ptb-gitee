#系统BL程序

def bootloader():
    import os
    import time
    print("BootLoader running....done")
    time.sleep(1)
    os.system("python3 sysver.py")
    print("System Staring....")
    print("Welcome to PyDos")
    print()
    print()
    print()
    print()


    os.system("python3 PyShell.py")

bootloader()