# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python-bubble-sort.html
Python 冒泡排序
"""

import pysnooper


@pysnooper.snoop()
def Sort(arr):
    s = len(arr)

    for x in range(s):
        for y in range(s - x - 1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    print(arr)
    return arr


def main():
    arr = [76543, 12345, 6543, 123, 91837, 2134, 32, 21, 43, 11, 84, 55]
    Sort(arr)


if __name__ == '__main__':
    main()