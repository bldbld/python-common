# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2972.py
# 
# Title: POJ GRIDS 2972 确定进制
# 
# Probleam Description:
# 6*9=42对于十进制来说是错误的，但是对于13进制来说是正确的。
# 即,6(13)*9(13)=42(13)，而42(13)=4*131+2*130=54(10)。
# 你的任务是写一段程序读入三个整数p、q和r，
# 然后确定一个进制B(2<=B<=16)使得p*q=r.如果B有很多选择,输出最小的一个。
# 例如：p=11,q=11,r=121.
# 则有11(3)*11(3)=121(3)因为11(3)=1*31+1*30=4(10)和121(3)=1*32+2*31+1*30=16(10)。
# 对于进制10,有11(10)*11(10)=121(10)。
# 这种情况下，应该输出3。
# 如果没有合适的进制，则输出0。
# 输入数据：
# 输入有T组测试样例。T在第一行给出。
# 每一组测试样例占一行，包含三个整数p、q、r。
# p、q、r的所有位都是数字，并且1<p、q、r<1,000,000。
# 输出要求：
# 对于每个测试样例输出一行。
# 该行包含一个整数：即使得p*q=r成立的最小的B。
# 如果没有合适的B，则输出0。
# 
# Input Example:
# 3  
# 6 9 42  
# 11 11 121  
# 2 2 2  
# 
# Output Example:
# 13  
# 3 
# 0 
# 
# Algorithm Description:
# 将输入的三个数字转换为十进制，通过计算十进制结果是否正确来判断进制。
# 转换原理：121 = 1*16*16 + 2*16 + 1
# 抽象出来即是：对于N进制，每一位都乘以基数的(N-1)此方，然后相加即得到十进制数值。
# 
# PS:
# 本题目的Probleam Description已经介绍了转换逻辑：
# 由于限制于TXT格式，所以形如4*131+2*130的表达式应理解为4*13+2*1，131和130即13的一次幂和13的零次幂。
# 
# Author: Ballad
# Date: 2011-08-26

for i in range( int(raw_input()) ):
    # 默认从而二进制开始循环匹配
    startByte = 2
    ipt = raw_input()
    # 确定开始循环匹配的进制
    for ip in ipt:
        if ip == ' ':
            continue
        if ( (int(ip) + 1) > startByte ):
            startByte = int(ip) + 1
    ipt = ipt.split(' ')
    # 存放输入的三个数字的十进制值
    a = [0,0,0]
    for j in range(startByte,18):
        # 通过判断进制值是否等于17来确认是否在16进制以内有结果
        if (j == 17):
            print '0'
            break
        # 分别计算每种进制下输入的三个数字的十进制值
        for k in range(3):
            a[k] = 0
            n = len(ipt[k]) - 1
            for ipk in ipt[k]:
                a[k] = a[k] + int(ipk) * pow(j,n)
                n = n - 1
        if (a[0]*a[1] == a[2]) :
            print j
            break
