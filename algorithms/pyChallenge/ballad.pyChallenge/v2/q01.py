# -*- coding: utf-8 -*-
'''
Q1:What about making trans?everybody thinks twice before solving this.
http://www.pythonchallenge.com/pc/def/map.html
题目的意思是将给定的字符串按照图中"K-M O-Q E-G"的方式替代，于是有了下面的方法：

Created on 2011-1-31

@author: bkin
'''
import string  

'''
第一种基本的方法。
'''
def foo1 ():
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    for s in str:
        if ord(s) == 121 or ord(s) == 122:
            s = chr(ord(s) - 24)
        elif 96 < ord(s) < 121:
            s = chr(ord(s) + 2)
        print s,

'''
string.maketrans()方法（我理解的）：
此方法返回一个table，用以指示intab和outtab两个字符串对应的替代位置，注意intab和outtab应具有相同长度。
''' 
def foo2 ():
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."  
    intab = "abcdefghijklmnopqrstuvwxyz"  
    outtab = "cdefghijklmnopqrstuvwxyzab"  
    transtab = string.maketrans(intab, outtab)  
    print str.translate(transtab)


if __name__ == '__main__':
    foo1()
    foo2()
