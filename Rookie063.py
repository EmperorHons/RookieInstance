# -*- coding = utf-8 -*-
# @Time : 2020/7/27 21:30
# @Author : EmperorHons
# @File : Rookie063.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-get-dayago.html
Python 获取几天前的时间
"""

import time
import datetime


def old_Time():
    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
    # 转换为时间戳
    timeStamp = int(time.mktime(threeDayAgo.timetuple()))
    # 转换为其他字符串格式
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    print(timeStamp)
    print(otherStyleTime)
    return otherStyleTime


if __name__ == '__main__':
    old_Time()