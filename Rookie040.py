# -*- coding = utf-8 -*-
# @Time : 2020/6/25 2:32
# @Author : EmperorHons
# @File : Rookie040.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-list-interchange.html
Python 将列表中的头尾两个元素对调
对调前 : [1, 2, 3]
对调后 : [3, 2, 1]
"""

import pysnooper


@pysnooper.snoop()
def swapList(newList):
    arr = newList
    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
    return newList


if __name__ == '__main__':
    newList = [1, 2, 3, 4]
    print(swapList(newList))
