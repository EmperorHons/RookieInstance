# -*- coding = utf-8 -*-
# @Time : 2020/6/27 22:44
# @Author : EmperorHons
# @File : Rookie042.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-reversing-list.html
Python 翻转列表
定义一个列表，并将它翻转。
"""

import pysnooper


@pysnooper.snoop()
def Reverse(newList):
    arr = newList
    arr.reverse()
    return arr


if __name__ == '__main__':
    newList = [23, 65, 19, 90]
    print(Reverse(newList))
