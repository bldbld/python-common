# 统计NS2模拟器的out.tr文件中丢包率
# from __future__ import division

file1 = open ("out.tr", "r")
calcd = 0
allp = 0
for line in file1.readlines():
    if line[0] == "d":
        calcd = calcd + 1
    allp = allp + 1
print calcd / allp  
