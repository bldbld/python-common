# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2807.py
# 
# Title: POJ GRIDS 2807 ���� 
# 
# Probleam Description:
# ����2��15����ͬ������������������Ǽ�����Щ�������ж��ٸ��������㣺
# ������һ��������һ������������
# �������1 4 3 2 9 7 18 22���õ��Ĵ���3����Ϊ2��1��������4��2��������18��9��������
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