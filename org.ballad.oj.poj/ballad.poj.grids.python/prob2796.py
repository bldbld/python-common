# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2796.py
# 
# Title: POJ GRIDS 2796 �������
# 
# Probleam Description:
# ����һ�������� a���Լ������ 5 ����������
# �����ǣ��� 5�������У�С�� a �������ĺ��Ƕ��٣� 
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