# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2753.py
# 
# Title: POJ GRIDS 2753 쳲���������
# 
# Probleam Description:
# 쳲�����������ָ���������У�
# ���еĵ�һ���͵ڶ�������Ϊ 1��������ÿ����������ǰ�� 2 ����֮�͡�
# ����һ�������� a��Ҫ��쳲����������е� a �����Ƕ��١� 
# 
# Input Example:
# 3
# Output Example:
# 2
# 
# Algorithm Description:
# ѭ��
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