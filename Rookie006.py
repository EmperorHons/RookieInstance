# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-area-of-a-circle.html  Python 计算圆的面积
"""

import math


def Area(r):

    s = math.pi * (r ** 2)
    print(math.pi)

    return s


print("圆的面积为: %.10f" % Area(5))