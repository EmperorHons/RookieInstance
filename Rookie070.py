# -*- coding = utf-8 -*-
# @Time : 2020/8/12 21:40
# @Author : EmperorHons
# @File : Rookie070.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-bubble-sort.html
Python 冒泡排序
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，
一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
"""
import pysnooper


@pysnooper.snoop()
def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    print("排序后的数组")
    for i in range(len(arr)):
        print("%d" % arr[i])


if __name__ == '__main__':
    main()