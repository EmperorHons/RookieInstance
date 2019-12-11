# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-random-number.html Python 随机数生成
"""
import random
import pysnooper


@pysnooper.snoop()
def Random():
    list = []
    for i in range(0, 9):
        s = random.randint(0, 9)
        list.append(s)
    print(list)
    return list