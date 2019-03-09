# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/8 19:08
# @File:14.py

'''
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述
数据输出n行，输出结果为按照字典序排列的字符串
'''
'''import sys
num=int(input())
while True:
    try:
        for i in range(num):
            string=sys.stdin.readline()'''

while True:
    try:
        num=int(input())
        L=[]
        for i in range(num):
            L.append(input())
            L=sorted(L)
        for i in L:
                print(i)
    except:
        break

