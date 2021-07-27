#帮助文件，修改于2021.7.15
print("PyDOS 帮助文档")
print("这是一个小工具集，我把它做成了一个类似于DOS的Shell（当然，它本身也是一个shell）")
print("您可以用内置的小工具进行任何工作，但各种工具仍在完善当中，在以后的更新中将提供（说不定还会做一个更新、安装插件的工具，暂定名称PPK(PyDOS Package)）")
print("")
print("")
print("1.ASCII转换工具 2.计算器 3.sys.ver工具 4.BootLoader 5.ADB 6.PyShell 7.PyMusic")
help = int(input("请选择一个以获取帮助："))

if help == 1 :
    print("ASCII工具")
    print("命令行输入'ASCII',然后根据提示输入字符，然后回车进行转换")
    print("此版本仅支持字符转ASCII")
    print("ASCII转换，0.0.2")
elif help == 2 :
    print("计算器")
    print("PyShell输入'calcutator',然后会打开一个窗口，即可进行运算")
    print("PyCalcutator, 0.0.1")
elif help == 3 :
    print("sys.ver工具")
    print("此工具可检测您的系统版本、软件版本号、Python版本，由sys、platform库实现")
    print("sys.ver，0.0.1 Beta")
elif help == 4 :
    print("Bootloader")
    print("现在看上去除了显示版本号似乎没有其他什么用....不过后期会有更多功能。")
    print("此程序待完善")
    print("BootLoader，0.0.1 In development")
elif help == 5 :
    print("ADB Shell")
    print("请自行前往Android Devloper官网查看使用方法，用PyShell使用还需一段时间开发。")
elif help ==6 :
    print("PyShell")
    print("PyDOS主体部分，功能还需完善(当然大多数功能都是软件包提供，它仅仅是一个管理器)，甚至可以直接运行cmd命令(只不过好像没有办法用cd命令,那得让提示符可修改....待解决)")
    print("PyShell 0.0.1 Dev")

elif help == 7 :
    print("PyMusic")
    print("PyMusic分PyMusicPlayer与PyMusicDownload组件")
    print("PyMusicPlayer:您可以在这里播放音乐，现支持*.mp3，可通过在PyShell输入Music打开")
    print("PyMusicDownload组件:您可以输入歌名下载音乐，音乐来自网易云音乐。可在PyMusicPlayer中点击  下载歌曲  打开")
    print("PyMusic 0.1")