# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2800.py
# 
# Title: POJ GRIDS 2800 垂直立方图
# 
# Probleam Description:
# 输入4行全部由大写字母组成的文本，输出一个垂直直方图，给出每个字符出现的次数。
# 注意：只用输出字符的出现次数，不用输出空白字符，数字或者标点符号的输出次数。 
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
# 将每种字母的出现次数记录在count数组中，然后循环打印出结果。
# 循环打印时，每次对count数组的记录减1，直到没有大于0的数据，打印结束。
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