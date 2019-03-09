# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/7 14:26
# @File:6.py

'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）

最后一个数后面也要有空格
详细描述：


函数接口说明：

public String getResult(long ulDataInput)

输入参数：

long ulDataInput：输入的正整数

返回值：

String

输入描述：
输入一个long型整数
输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
'''

num=int(input())
i=2
while i*i<num:
    if num%i==0:
        print(str(i),end=' ')#end缺省值是换行
        num=num//i#//表示整数相除，返回一个不大于结果的最大整数
        i=2
    else:
        i+=1
print(str(num),end=' ')
