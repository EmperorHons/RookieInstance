# -*- coding = utf-8 -*-
# @Time : 2020/7/30 21:44
# @Author : EmperorHons
# @File : Rookie.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-linear-search.html
Python 线性查找
线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。
"""

import pysnooper


@pysnooper.snoop()
def search(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1;


def main():
    # 在数组 arr 中查找数字10
    arr = [1, 14, 21, 32, 81, 10, 12]
    x = 10
    n = len(arr)
    result = search(arr, n, x)
    if result == -1:
        print("元素不在数组中")
    else:
        print("元素在数组中的索引为：", result)


if __name__ == '__main__':
    main()