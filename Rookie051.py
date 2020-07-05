# -*- coding = utf-8 -*-
# @Time : 2020/7/5 20:00
# @Author : EmperorHons
# @File : Rookie051.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/pyhton-remove-ith-character-from-string.html
Python 移除字符串中的指定位置字符
"""

import pysnooper


@pysnooper.snoop()
def remove_String(test_str):
    new_str = ""
    for i in range(len(test_str)):
        if i != 2:
            new_str = new_str + test_str[i]
    return new_str


if __name__ == '__main__':
    test_str = "Original string"
    print(remove_String(test_str))
