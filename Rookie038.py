# -*- coding = utf-8 -*-
# @Time : 2020/6/21 23:03
# @Author : EmperorHons
# @File : Rookie038.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python3-sum-array.html
Python 计算数组元素之和
L = (x, y, z)
s = x + y +z
"""

import pysnooper


@pysnooper.snoop()
def Array_Sum():
    t = (1, 2, 3, 100)
    s = 0
    for i in t:
        s += i
    print(s)


if __name__ == '__main__':
    Array_Sum()
