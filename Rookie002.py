# -*- coding:utf-8 -*-
"""
https://www.runoob.com/python3/python3-add-number.html Python 数字求和
"""

num1 = input("请输入第一个数字： ")
num2 = input("请输入第二个数字： ")

sum = float(num1) + float(num2)

print("数字{0}和{1}相加的结果为： {2}".format(num1, num2, sum))

print('两数之和为 %.1f' % (float(input("请输入第一个数字： ")) + float(input("请输入第二个数字： "))))