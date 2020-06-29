# -*- coding = utf-8 -*-
# @Time : 2020/6/29 21:43
# @Author : EmperorHons
# @File : Rookie045.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-clear-list.html
Python 复制列表
"""

list1 = [1, 7, 33, 21, 19]

# -----第一种方法-----
list2 = list1[:]
print(list2)

# -----第二种方法-----
list3 = []
list3.extend(list1)
print(list3)

# -----第三种方法-----
list4 = list(list1)
print(list4)
