# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2714.py
# 
# Title: POJ GRIDS 2714 平均年龄
# 
# Probleam Description:
# 班上有学生若干名，给出每名学生的年龄（整数），求班上所有学生的平均年龄，保留到小数点后两位。 
# 
# Input Example:
# 19 23 17 20 25 18
# Output Example:
# 23.33
# 
# Algorithm Description:
# 每次对取余结果*10，再取余。
# 结果未作四舍五入处理。
# 
# Author: Ballad
# Date: 2011-08-25

ipt = raw_input().split(' ')
totalAge = 0
for i in ipt:
    totalAge = totalAge + int(i)
aveAge = totalAge/len(ipt)
dicm = [0,0]
m = totalAge%len(ipt)
for i in range(2):
    m = m*10
    dicm[i] = m/len(ipt)
    m = m%len(ipt)
print '%d.%d%d' % (aveAge, dicm[0], dicm[1])