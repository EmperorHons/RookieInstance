# -*- coding = utf-8 -*-
# @Time : 2020/7/21 22:28
# @Author : EmperorHons
# @File : Rookie059.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-sum-dictionary.html
Python 计算字典值之和
给定一个字典，然后计算它们所有数字值的和
"""

import pysnooper


@pysnooper.snoop()
def my_Dict(myDict):
    sum = 0
    for i in myDict:
        sum += myDict[i]
        print(myDict[i])
    print(sum)
    return sum


if __name__ == '__main__':
    myDict = {'a': 100, 'b': 200, 'c': 300}
    my_Dict(myDict)