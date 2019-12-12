# -*- coding:utf-8 -*-
"""
https://www.runoob.com/python3/python3-factorial.html  Python 阶乘实例
"""
import pysnooper


@pysnooper.snoop()
def factorial():
    num = int(input("请输入一个数字： "))
    factorial = 1

    if num < 0:
        print("抱歉，复数没有阶乘")
    elif num == 0:
        print("0 的阶乘为1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("%d 的阶乘为 %d " % (num, factorial))


if __name__ == '__main__':
    factorial()
