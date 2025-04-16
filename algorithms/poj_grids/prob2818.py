# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2818.py
# 
# Title: POJ GRIDS 2818 Bob&Alice�ļ���
# 
# Probleam Description:
# Bob�� Alice��ʼʹ��һ��ȫ�µı���ϵͳ������һ�ֻ���һ��˽��Կ�׵ġ�
# ����ѡ����n����ͬ����a1;...;an,���Ƕ�����0С�ڵ���n��
# ���ܹ������£�
# �����ܵ���Ϣ�������������Կ���£���Ϣ�е��ַ�����Կ�е�����һһ��Ӧ������
# ��Ϣ��λ��iλ�õ���ĸ����д��������Ϣ�ĵ�ai��λ��,ai��λ��iλ�õ���Կ��
# ������Ϣ��˷������ܣ�һ������k�Ρ�
# ��Ϣ����С�ڵ���n�������Ϣ��n��,�����λ���ÿո��ֱ����Ϣ����Ϊn��
# �������Alice��Bobдһ�����򣬶�����Կ��Ȼ�������ܴ���k��Ҫ���ܵ���Ϣ�������ܹ�����Ϣ���ܡ�
# 
# Input Example:
# 10
# 1 3 9 4 10 8 6 2 5 7
# 15
# THISISWHO
# 
# Output Example:
# TIOS HSHIW
# 
# Algorithm Description:
# 
# 
# 
# Author: Ballad
# Date: 2011-08-26

# ��Կ����n
n = int(raw_input())
# ��Կ����
a = raw_input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i]) - 1
# ���ܴ���
k = int(raw_input())
# msg ����
msg = []
# crypt ����
crypt = []
for ip in raw_input():
    msg.append(ip)
    crypt.append(ip)
# ���������Ϣ����С��n���Ҳ��ո�
if len(msg) < n:
    for i in range(len(msg),n):
        msg.append(' ')
        crypt.append(' ')
for ki in range(k):
    for i in range(n):
        msg[i] = crypt[i]
    for i in range(n):
        crypt[a[i]] = msg[i]
str = ''
for ci in crypt:
    str = str + ci
print str
