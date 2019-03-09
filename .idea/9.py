# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/8 13:40
# @File:9.py

'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
输入描述：
输入一个int型整数
输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
'''

num=input()
L=list(reversed(num))
#print(L)
res=[]
for i in L:
    if i not in res:
        res.append(i)
print("".join(res))

