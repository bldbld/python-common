# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2807.py
# 
# Title: POJ GRIDS 2807 两倍 
# 
# Probleam Description:
# 给定2到15个不同的正整数，你的任务是计算这些数里面有多少个数对满足：
# 数对中一个数是另一个数的两倍。
# 比如给定1 4 3 2 9 7 18 22，得到的答案是3，因为2是1的两倍，4是2个两倍，18是9的两倍。
# 
# Input Example:
# 1 4 3 2 9 7 18 22
# Output Example:
# 3
# 
# Algorithm Description:
#  
# Author: Ballad
# Date: 2011-08-26

ipt = raw_input().split(' ')
i = 0
for ip in ipt :
    ipt[i] = int(ip)
    i = i + 1
count = 0
for ip in ipt :
    if ip*2 in ipt:
        count = count + 1
print count