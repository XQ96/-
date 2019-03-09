# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/8 19:34
# @File:15.py
'''
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数
输入描述：
输入一个整数（int类型）
输出描述
这个数转换成2进制后，输出1的个数
'''

num=int(input())
num=bin(num).replace('0b','')
L=list(num)
res=[]
for i in L:
    if (int(i)==1):
       res.append(i)
    else:
        res=res
print(len(res))

