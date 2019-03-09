# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/7 11:17
# @File:4.py
'''
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)
输出描述：
输出到长度为8的新字符串数组
'''
import sys
a=sys.stdin.readline().strip()
b=sys.stdin.readline().strip()
c=[a[i:i+8] for i in range(0,len(a),8)]
d=[b[i:i+8] for i in range(0,len(b),8)]
L=c+d
for i in L:
    if len(i)<8:
        x=i+'0'*(8-len(i))# *表示倍数
        print(x)
    else:
        print(i)