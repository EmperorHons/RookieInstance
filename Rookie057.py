# -*- coding = utf-8 -*-
# @Time : 2020/7/15 22:58
# @Author : EmperorHons
# @File : Rookie057.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-slicing-rotate-string.html
Python 对字符串切片及翻转
给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。
"""

import pysnooper


@pysnooper.snoop()
def string_Rotate(input, d):

    Lfirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0:len(input)-d]
    Rsecond = input[len(input)-d:]

    print("头部切片反转 : ", (Lsecond + Lfirst))
    print("尾部切片反转 : ", (Rsecond + Rfirst))


if __name__ == '__main__':
    input = "Runoob"
    d = 2  # 截取两个字符
    string_Rotate(input, d)