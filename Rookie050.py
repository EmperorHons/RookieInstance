# -*- coding = utf-8 -*-
# @Time : 2020/7/5 19:30
# @Author : EmperorHons
# @File : Rookie050.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-max-list-element.html
Python 查找列表中最大元素
输入 : list1 = [10, 20, 4]
输出 : 20
"""

import pysnooper


@pysnooper.snoop()
def max_Number(List):
    return max(List)


if __name__ == '__main__':
    List = [1, 5, 2, 44, 82,13, 26, 57]
    print(max_Number(List))