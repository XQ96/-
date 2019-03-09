# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/7 10:39
# @File:3.py
'''
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
Input Param

n               输入随机数的个数

inputArray      n个随机整数组成的数组


Return Value

OutputArray    输出处理后的随机整数


'''
import sys
while True:
    try:
        n=int(sys.stdin.readline().strip('\n'))
        L=[]
        for i in range(n):
            num=int(sys.stdin.readline().strip('\n'))
            L.append(num)
        a=list(set(L))
        b=sorted(a)
        for i in b:#注意py遍历数组list特别方便直接遍历，range针对一个的、范围
            print(i)
    except:
        break