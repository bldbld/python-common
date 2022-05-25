# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2796.py
# 
# Title: POJ GRIDS 2796 数字求和
# 
# Probleam Description:
# 给定一个正整数 a，以及另外的 5 个正整数，
# 问题是：这 5个整数中，小于 a 的整数的和是多少？ 
# 
# Input Example:
# 17
# 1 2 3 17 19
# Output Example:
# 6
# 
# Algorithm Description:
# 
# 
# Author: Ballad
# Date: 2011-08-26

a = int( raw_input() )
ipt = raw_input().split(' ')
count = 0
for i in ipt :
    if int(i) < a:
        count = count + int(i)
print count