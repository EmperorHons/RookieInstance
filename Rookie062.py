# -*- coding = utf-8 -*-
# @Time : 2020/7/26 21:29
# @Author : EmperorHons
# @File : Rookie062.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-str-timestamp.html
Python 将字符串的时间转换为时间戳
给定一个字符串的时间，将其转换为时间戳。
"""

import time
import pysnooper


@pysnooper.snoop()
def time_Change():
    a1 = "2020-07-26 21:29:00"
    # 先转换为时间数组
    timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

    # 转换为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)


if __name__ == '__main__':
    time_Change()