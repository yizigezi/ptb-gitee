sysVer = "PyDOS 0.0.2 Dev  PyShell 0.0.1 Dev    Build at 2021.7.17"
print(sysVer)

import sys, platform

a = sys.version_info
print("Python Version: {a[0]}.{a[1]}.{a[2]}".format(a=a))

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
print("OS:{ret[plat_form]}".format(ret=ret))
print("OS Version: {ret}".format(ret=ret['version'].split(" ")[0]))
print("{ret[version_bit]}Bit OS".format(ret=ret))

print("本项目基于GPL 3.0开源协议")