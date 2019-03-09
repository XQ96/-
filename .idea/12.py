# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/8 15:49
# @File:12.py
'''
题目描述
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。例如：
输入描述：
输入N个字符
输出描述：
输出该字符串反转后的字符串
'''

string=input()
L=list(reversed(string))
#print(L)
res=[]
for i in L:
    res.append(i)
print(''.join(res))