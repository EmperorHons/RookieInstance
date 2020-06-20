# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-99-table.html  Python 九九乘法表
"""
import pysnooper


# @pysnooper.snoop()
def ChengFa():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i*j), end=' ')
        print()


if __name__ == '__main__':
    ChengFa()
