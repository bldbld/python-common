# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2800.py
# 
# Title: POJ GRIDS 2800 ��ֱ����ͼ
# 
# Probleam Description:
# ����4��ȫ���ɴ�д��ĸ��ɵ��ı������һ����ֱֱ��ͼ������ÿ���ַ����ֵĴ�����
# ע�⣺ֻ������ַ��ĳ��ִ�������������հ��ַ������ֻ��߱����ŵ���������� 
# 
# Input Example:
# DAFLJLAFAE
# FAEIUHFAEF
# FAEEA
# FAEFEIAELQBVEAEQP
# 
# Output Example:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * *   * * *   * * *   *       * *       * *
# *       * *     *     *         *
# *       * *           *
# *       * *
# *       * *
# *       * *
# *       * *
# *       * *
# *       *
# *       *
# 
# Algorithm Description:
# ��ÿ����ĸ�ĳ��ִ�����¼��count�����У�Ȼ��ѭ����ӡ�������
# ѭ����ӡʱ��ÿ�ζ�count����ļ�¼��1��ֱ��û�д���0�����ݣ���ӡ������
# 
# Author: Ballad
# Date: 2011-08-26

ipt = ['','','','']
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(4):
    ipt[i] = raw_input()
    for ip in ipt[i]:
        tmp = ord(ip) - 65
        count[tmp] = count[tmp] + 1
print 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
isPrint = True
while isPrint:
    isPrint = False
    str = ''
    for i in range(26):
        if count[i] > 0:
            str = str + '* '
            if count[i] > 1:
                isPrint = True
        else:
            str = str + '  '
        count[i] = count[i] - 1
    print str