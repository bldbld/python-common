# 将当前时间和CPU空闲率 （平均值）保存在/var/log下 格式“年-月-日”
import time
import os

if __name__ == "__main__":
    now = time.localtime(time.time())
    cpu = os.popen('sar -u 1 5')
    cpuusages = cpu.readlines()
    cpuusageidle = cpuusages[6]
    idle = cpuusageidle.split("     ")
    idletrim = idle[7].split('%')
    idlefloat = float(idletrim[0])
    usefloat = 100.0 - idlefloat
    writedata = "%d-%d-%f" % (now.tm_hour, now.tm_min, usefloat)
    filename = "%d-%d-%d" % (now.tm_year, now.tm_mon, now.tm_mday)
    pathname = "/var/log/" + filename
    filew = open(pathname, 'w')
    filew.write(writedata)
    filew.close()
