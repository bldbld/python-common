# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob1017.py
# 
# Title: POJ GRIDS 1017 装箱问题
# 
# Probleam Description:
# 
# Input Example:
# 0 0 4 0 0 1
# 7 5 1 0 0 0
# 0 0 0 0 0 0
# 
# Output Example:
# 2
# 1
# 
# Algorithm Description:
# 6*6,5*5,4*4的产品各占一个箱子。
# 4个3*3的产品占一个箱子，剩余的3*3产品装入一个箱子，所剩空间因剩余数而不同。
# 2*2产品可以放进4*4和剩余3*3所占箱子的剩余空间。
# 1*1产品只要有剩余空间，就可以存放。
# 首先计算出6*6,5*5,4*4,3*3占了多少箱子，
# 然后计算4*4和剩余3*3产品所剩余空间能否装下2*2产品，
# 如果上面计算后的空间仍有剩余，则计算1*1时剩余空间应加上此处的剩余空间，
# 然后计算5*5,剩余3*3(假设已放满2*2产品的情况)和上面剩余的空间能否装下1*1产品，
# 最后，如果2*2和1*1的产品有装不下情况，使用新的箱子盛放，
# 此处只需算出全部剩余2*2和1*1产品所需的空间，并分配箱子即可。
# 
# Author: Ballad
# Date: 2011-08-25

# bc: 存放3*3的产品对4取余后剩余的空间所能盛放的2*2产品数
bc = [0,5,3,1]
# ac: 存放3*3的产品对4取余后剩余的空间再放满2*2产品后所能盛放的1*1产品数
ac = [0,7,6,5]
while True:
    # ipt: Input Value 输入数据
    ipt = raw_input().split(' ')
    i = 0
    # isBreak: 是否中断循环(输入数据是否全为0)
    isBreak = True
    for si in ipt:
        ipt[i] = int (si)
        if ipt[i] != 0:
            isBreak = False
        i = i + 1
    if isBreak:
        break
    # count: 统计的箱子数目
    count = ipt[5] + ipt[4] + ipt[3] + ipt[2]/4
    # j: 临时变量，用于存放取余结果
    j = ipt[2]%4
    if j != 0:
        count = count + 1
    # b: 用2*2产品总数减去4*4,3*3(见bc数组)产品所剩余的空间
    b = ipt[1] - ipt[3]*5 - bc[j]
    # a: 用1*1产品总数减去5*5,3*3(见ac数组),放满2*2后剩余空间(如果有的话)所剩余的空间
    if b < 0:
        a = ipt[0] - (ipt[4]*11 + ac[j] - b*4)
        if a > 0:  
            count = count + a/36
            if a%36 != 0:
                count = count + 1
    else:
        a = ipt[0] - (ipt[4]*11 + ac[j])
        if a > 0:
            # t: 临时变量，用于存放取余结果
            t = b*4 + a 
            count = count + t/36
            if t%36 != 0:
                count = count + 1
        else:
            count = count + b/8
            if b%8 != 0:
                count = count + 1
    print count
