# -*- coding:utf-8 -*-
"""
https://www.runoob.com/python3/python3-area-triangle.html  Python 计算三角形的面积
"""
# 海伦公式计算三角形的面积
a = float(input('输入三角形第一边长： '))
b = float(input('输入三角形第二边长： '))
c = float(input('输入三角形第三边长： '))

# 计算半周长
s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)
