# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2714.py
# 
# Title: POJ GRIDS 2714 ƽ������
# 
# Probleam Description:
# ������ѧ��������������ÿ��ѧ�������䣨�����������������ѧ����ƽ�����䣬������С�������λ�� 
# 
# Input Example:
# 19 23 17 20 25 18
# Output Example:
# 23.33
# 
# Algorithm Description:
# ÿ�ζ�ȡ����*10����ȡ�ࡣ
# ���δ���������봦��
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