# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2753.py
# 
# Title: POJ GRIDS 2753 斐波那契数列
# 
# Probleam Description:
# 斐波那契数列是指这样的数列：
# 数列的第一个和第二个数都为 1，接下来每个数都等于前面 2 个数之和。
# 给出一个正整数 a，要求斐波那契数列中第 a 个数是多少。 
# 
# Input Example:
# 3
# Output Example:
# 2
# 
# Algorithm Description:
# 循环
# 
# 
# Author: Ballad
# Date: 2011-08-26

a = int( raw_input() )
if a == 1 or a == 2:
    print 1
else:
    f = 1
    s = 1
    for i in range(3,a+1):
        t = s + f
        f = s 
        s = t
    print t