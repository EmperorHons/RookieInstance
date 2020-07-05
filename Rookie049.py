# -*- coding = utf-8 -*-
# @Time : 2020/7/5 19:26
# @Author : EmperorHons
# @File : Rookie049.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-min-list-element.html
Python 查找列表中最小元素
输入 : list1 = [10, 20, 4]
输出 : 4
"""

import pysnooper


@pysnooper.snoop()
def min_Number(List):
    return min(List)


if __name__ == '__main__':
    List = [1, 5, 2, 44, 13, 26, 57, 82]
    print(min_Number(List))