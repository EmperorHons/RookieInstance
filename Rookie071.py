# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python-bubble-sort.html  Python 冒泡排序
"""

l = [76543, 12345, 6543, 123, 91837, 2134, 32, 21, 43, 11, 84, 55]
s = len(l)

for x in range(s):
    for y in range(s - x - 1):
        if l[y] > l[y + 1]:
            l[y], l[y + 1] = l[y + 1], l[y]
print(l)
