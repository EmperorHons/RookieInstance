# -*- coding = utf-8 -*-
# @Time : 2020/7/20 22:19
# @Author : EmperorHons
# @File : Rookie058.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html
Python 按键(key)或值(value)对字典进行排序
给定一个字典，然后按键(key)或值(value)对字典进行排序。
"""

import pysnooper


# 按键(key)排序
@pysnooper.snoop()
def dictionairy1():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按键(key)排序：")

    # sorted(key_value) 返回一个迭代器
    # 字典按键排序
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


# 按值(value)排序
def dictionairy2():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print('\n', "按值(value)排序：")

    # sorted(key_value) 返回一个迭代器
    # 字典按键排序
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))


if __name__ == '__main__':
    dictionairy1()
    dictionairy2()