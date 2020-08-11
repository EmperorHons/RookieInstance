# -*- coding = utf-8 -*-
# @Time : 2020/8/10 21:49
# @Author : EmperorHons
# @File : Rookie069.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-selection-sort.html
Python 选择排序
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
"""

import pysnooper


@pysnooper.snoop()
def Select_sort(List):
    for i in range(len(List)):
        min_dix = i
        # print("i的值", i)
        for j in range(i+1, len(List)):
            # print("j的值", j)
            if List[min_dix] > List[j]:
                min_dix = j

        List[i], List[min_dix] = List[min_dix], List[i]
    print("排序后的数组：")
    for i in range(len(List)):
        print("%d" % List[i]),
    return List[i]


if __name__ == '__main__':
    List = [64, 25, 12, 22, 11]
    Select_sort(List)