# -*- coding = utf-8 -*-
# @Time : 2020/7/23 22:48
# @Author : EmperorHons
# @File : Rookie061.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-merging-two-dictionaries.html
Python 合并字典
"""

import pysnooper


@pysnooper.snoop()
def Merge(dict1, dict2):
    return dict2.update(dict1)


@pysnooper.snoop()
def Res(dict1, dict2):
    res = {**dict1, **dict2}
    return res


if __name__ == '__main__':
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    print(Merge(dict1, dict2), dict2)
    print(Res(dict1, dict2))
