# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/8 15:28
# @File:10.py
'''
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。
输出描述：
输出范围在(0~127)字符的个数。
'''

string=input()
L=list(string)
res=[]
count=0
for i in L:
    if i not in res:
        res.append(i)
        count+=1
    else:
        count=count
print(count)
