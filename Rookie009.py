# -*- coding:utf-8 -*-
"""
https://www.runoob.com/python3/python3-swap-variables.html Python 交换变量
"""

x = input('输入x值：')
y = input('输入y值：')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后x的值为：{}'.format(x))
print('交换后y的值为：{}'.format(y))


# 不使用临时变量交换
x, y = y, x

print('交换后x的值为：{}'.format(x))
print('交换后y的值为：{}'.format(y))