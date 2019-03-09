# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/7 19:09
# @File:7.py

import math
def get_value(a):
    a=float(a)
    decimal=a-int(a)
    if (decimal*10)>=5:
        return math.ceil(a)
    else:
        return math.floor(a)


if __name__=='__main__':
    case=input()
    print(get_value(case))

#math.ceil()
#math.floor()
