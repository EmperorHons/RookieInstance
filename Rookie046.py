# -*- coding = utf-8 -*-
# @Time : 2020/6/30 22:33
# @Author : EmperorHons
# @File : Rookie046.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-count-occurrences-element-list.html
Python 计算元素在列表中出现的次数
"""

import pysnooper


@pysnooper.snoop()
def List(list, x):
    i = 0
    for l in list:
        if l == x:
            i += 1
    return i


if __name__ == '__main__':
    list = [1, 3, 5, 2, 3, 7, 43, 3, 9, 11, 3]
    x = 3
    print(List(list, x))