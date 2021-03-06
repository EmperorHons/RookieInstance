# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-prime-number-intervals.html  Python 输出指定范围内的素数
"""
import pysnooper


@pysnooper.snoop()
def PrimeNumber():
    lower = int(input("输入区间最小值："))
    upper = int(input("输入区间最大值："))

    for num in range(lower, upper + 1):
        # 素数大于1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        return num


PrimeNumber()
