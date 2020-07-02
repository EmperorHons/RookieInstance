# -*- coding = utf-8 -*-
# @Time : 2020/7/2 22:10
# @Author : EmperorHons
# @File : Rookie048.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-multiply-list.html
Python 计算列表元素之积
"""

import pysnooper


@pysnooper.snoop()
def List_Product(List):
    s = 1
    for i in List:
        p = s * i
    return p


if __name__ == '__main__':
    List = [1, 5, 2, 44, 13, 26, 39, 57, 82]
    print(List_Product(List))
