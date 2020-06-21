# -*- coding = utf-8 -*-
# @Time : 2020/6/20 15:04
# @Author : EmperorHons
# @File : Rookie037.py
# @Software : PyCharm

"""
https://www.runoob.com/python3/python-cube-sum.html
Python 计算 n 个自然数的立方和
计算公式 13 + 23 + 33 + 43 + …….+ n3
"""
七
import pysnooper


@pysnooper.snoop()
def sum_series():
    a = int(input("请输入你的数字："))
    sum = 0
    for i in range(1, a + 1):
        sum += i * i * i
        i += 1
    return sum


if __name__ == '__main__':
    print(sum_series())