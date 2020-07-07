# -*- coding = utf-8 -*-
# @Time : 2020/7/7 22:18
# @Author : EmperorHons
# @File : Rookie053.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-string-length.html
Python 判断字符串长度
"""

import pysnooper


# @pysnooper.snoop()
def string_Number(string):
    s = len(string)
    return s


@pysnooper.snoop()
def find_Len(string):
    i = 0
    while string[i:]:
        # print(i)
        # print(string[i:])
        i += 1
    return i


if __name__ == '__main__':
    string = "stringNumber"
    print(string_Number(string))
    print(find_Len(string))
