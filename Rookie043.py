# -*- coding = utf-8 -*-
# @Time : 2020/6/28 22:12
# @Author : EmperorHons
# @File : Rookie043.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-check-element-exists-in-list.html
Python 判断元素是否在列表中存在
"""

import pysnooper


@pysnooper.snoop()
def if_into(List):
    s = 5
    for i in range(len(List)):
        if s == List[i]:
            print("元素在列表中")
        else:
            None
    return


if __name__ == '__main__':
    List = [31, 3, 5, 13, 19]
    if_into(List)
