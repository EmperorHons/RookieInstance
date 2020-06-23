# -*- coding = utf-8 -*-
# @Time : 2020/6/23 22:52
# @Author : EmperorHons
# @File : Rookie039.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python3-array-rotation.html
Python 数组翻转指定个数的元素
例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
"""

import pysnooper


@pysnooper.snoop()
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


@pysnooper.snoop()
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    print(temp)


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 11, 16, 43, 66]
    leftRotate(arr, 2, len(arr))
    printArray(arr, len(arr))
