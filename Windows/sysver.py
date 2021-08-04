import sys, platform, time

sysVer = "PyDOS 0.1 Beta  PyShell 1.0  Build at 2021.7.27"
print(sysVer)

a = sys.version_info
print("Python Runtime Ver: {a[0]}.{a[1]}.{a[2]}".format(a=a))

ret = {}

plat_form = platform.platform()
if "Linux" in plat_form:
    ret["plat_form"] = "Linux"
elif "Windows" in plat_form:
    ret["plat_form"] = "Windows"
else:
    ret['plat_form'] = "Mac"

ret["version"] = platform.version()
ret['version_bit'] = platform.architecture()[0][0:2]
print("*Platform OS:{ret[plat_form]}".format(ret=ret))
print("*Platform OS Version: {ret}".format(ret=ret['version'].split(" ")[0]))
print("*{ret[version_bit]}Bit OS".format(ret=ret))

print("本项目基于GPL 2.0开源协议")

date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print("*System information as of ", date)