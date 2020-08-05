# -*- coding = utf-8 -*-
# @Time : 2020/8/5 22:38
# @Author : EmperorHons
# @File : Rookie066.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-insertion-sort.html
Python 插入排序
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，
在已排序序列中从后向前扫描，找到相应位置并插入。
"""

import pysnooper


@pysnooper.snoop()
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            print("比较前的key:", key)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("比较后的key:", key)


arr = [12, 11, 27, 41, 22, 94]
insertionSort(arr)
print("排序后的数组：")
for i in range(len(arr)):
    print("%d" % arr[i])
