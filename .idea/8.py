# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/7 19:43
# @File:8.py

'''
题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
输入描述：
先输入键值对的个数
然后输入成对的index和value值，以空格隔开
输出描述：
输出合并后的键值对（多行）
'''

num=int(input())#input默认是str
def change(num):
    key_value={}
    for i in range(num):
        key,value=input().split(' ')
        key=int(key)
        value=int(value)
        if(key in key_value):
            key_value[key]+=value
        else:
            key_value[key]=value
    for x,y in key_value.items():
        print(x,y)

change(num)

