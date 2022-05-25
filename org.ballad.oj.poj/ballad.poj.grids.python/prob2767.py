# -*- coding:utf-8 -*-
# Python Version: 2.6
# File Name: prob2767.py
# 
# Title: POJ GRIDS 2767 Caesar����
# 
# Probleam Description:
# Julius Caesar����ʹ�ù�һ�ֺܼ򵥵����롣
# ���������е�ÿ���ַ�������������ĸ���к� 5 λ��Ӧ���ַ������棬�����͵õ������ġ�
# �����ַ� A �� F �����档���������ĺ��������ַ��Ķ�Ӧ��ϵ��  
# ����  
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
# ����  
# V W X Y Z A B C D E F G H I J K L M N O P Q R S T U  
# ��������ǶԸ��������Ľ��н��ܵõ����ġ�  
# ����Ҫע����ǣ������г��ֵ���ĸ���Ǵ�д��ĸ��
# ������Ҳ��������ĸ���ַ�������Щ�ַ����ý��н��롣 
# 
# Input Example:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Output Example:
# V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# 
# Algorithm Description:
# ƫ������ȡֵ������F��Ϊ��A��������ASCII���С��5������ƫ����Ϊ-5
# 
# 
# Author: Ballad
# Date: 2011-08-26

# Caesarƫ����
EXCURSION = -5
ipt = raw_input()
str = ''
for ip in ipt:
    # ���ڴ�д��ĸ���н���
    if ( ord(ip) > 64 and ord(ip) < 91 ):
        str = str + chr ( 65 + (ord(ip) - 65 + EXCURSION)%26 )
    else:
        str = str + ip
print str