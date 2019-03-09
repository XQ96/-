# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/7 0:22
# @File:2.py
'''
题目描述
    写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
输入描述：
    输入一个有字母和数字以及空格组成的字符串，和一个字符
输出描述：
    输出输入字符串中含有该字符的个数
'''
sourceStr=input()
inputStr=input()

sourceStrLower=sourceStr.lower()
inputStrLower=inputStr.lower()

num=0;
for i in range(len(sourceStrLower)):
    if inputStrLower==sourceStrLower[i]:
        num+=1;

print(num)