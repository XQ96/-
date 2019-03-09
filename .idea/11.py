# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/8 15:37
# @File:11.py

'''
题目描述
描述：

输入一个整数，将这个整数以字符串的形式逆序输出

程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

输入描述：
输入一个int整数
输出描述：
将这个整数以字符串的形式逆序输出
'''
num=input()
L=list(reversed(num))
res=[]
for i in L:
    res.append(i)
print("".join(L))