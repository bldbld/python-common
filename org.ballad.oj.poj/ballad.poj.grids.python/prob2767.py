# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2767.py
# 
# Title: POJ GRIDS 2767 Caesar密码
# 
# Probleam Description:
# Julius Caesar曾经使用过一种很简单的密码。
# 对于明文中的每个字符，将它用它字母表中后 5 位对应的字符来代替，这样就得到了密文。
# 比如字符 A 用 F 来代替。如下是密文和明文中字符的对应关系。  
# 密文  
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
# 明文  
# V W X Y Z A B C D E F G H I J K L M N O P Q R S T U  
# 你的任务是对给定的密文进行解密得到明文。  
# 你需要注意的是，密文中出现的字母都是大写字母。
# 密文中也包括非字母的字符，对这些字符不用进行解码。 
# 
# Input Example:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Output Example:
# V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# 
# Algorithm Description:
# 偏移量的取值：比如F变为了A，则它的ASCII码减小了5，所以偏移量为-5
# 
# 
# Author: Ballad
# Date: 2011-08-26

# Caesar偏移量
EXCURSION = -5
ipt = raw_input()
str = ''
for ip in ipt:
    # 对于大写字母进行解密
    if ( ord(ip) > 64 and ord(ip) < 91 ):
        str = str + chr ( 65 + (ord(ip) - 65 + EXCURSION)%26 )
    else:
        str = str + ip
print str