# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-square-root.html Python 平方根
"""
import cmath

# 正数的平方根
num = int(input("请输入一个数字： "))

num_sqrt = num ** 0.5

print("{0}的平方根为{1:0.3f}".format(num, num_sqrt))


# 负数/复数的平方根
num = int(input("请输入一个数字： "))

num_sqrt = cmath.sqrt(num)

print("{0}的平方根为{1:0.3f} + {2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))

