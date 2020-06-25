# -*- coding = utf-8 -*-
# @Time : 2020/6/25 23:15
# @Author : EmperorHons
# @File : Rookie041.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python3-list-swap-two-elements.html
Python 将列表中的指定位置的两个元素对调
对调前 : List = [23, 65, 19, 90],
对调后 : [19, 65, 23, 90]
"""

import pysnooper


@pysnooper.snoop()
def swapPositions(newList, L1, L2):
    arr = newList
    arr[L1], arr[L2] = arr[L2], arr[L1]
    return arr


if __name__ == '__main__':
    newList = [23, 65, 19, 90]
    print(swapPositions(newList, 1, 3))