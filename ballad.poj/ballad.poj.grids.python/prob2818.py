# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2818.py
# 
# Title: POJ GRIDS 2818 Bob&Alice的加密
# 
# Probleam Description:
# Bob和 Alice开始使用一种全新的编码系统。它是一种基于一组私有钥匙的。
# 他们选择了n个不同的数a1;...;an,它们都大于0小于等于n。
# 机密过程如下：
# 待加密的信息放置在这组加密钥匙下，信息中的字符和密钥中的数字一一对应起来。
# 信息中位于i位置的字母将被写到加密信息的第ai个位置,ai是位于i位置的密钥。
# 加密信息如此反复加密，一共加密k次。
# 信息长度小于等于n。如果信息比n短,后面的位置用空格填补直到信息长度为n。
# 请你帮助Alice和Bob写一个程序，读入密钥，然后读入加密次数k和要加密的信息，按加密规则将信息加密。
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

# 密钥长度n
n = int(raw_input())
# 密钥数组
a = raw_input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i]) - 1
# 加密次数
k = int(raw_input())
# msg 明文
msg = []
# crypt 密文
crypt = []
for ip in raw_input():
    msg.append(ip)
    crypt.append(ip)
# 如果输入信息长度小于n，右补空格
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
