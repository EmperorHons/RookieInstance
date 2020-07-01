# -*- coding = utf-8 -*-
# @Time : 2020/7/1 22:56
# @Author : EmperorHons
# @File : Rookie047.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-sum-list.html
Python 计算列表元素之和
定义一个数字列表，并计算列表元素之和。
例如： 输入 : [12, 15, 3, 10] 输出 : 40
"""

import pysnooper


@pysnooper.snoop()
def List_sum(List):
    s = 0
    for i in range(0, len(List) - 1):
        s += List[i]
        i += 1
    return s


if __name__ == '__main__':
    List = [1, 5, 2, 44, 13, 26, 39, 57, 82]
    print(List_sum(List))