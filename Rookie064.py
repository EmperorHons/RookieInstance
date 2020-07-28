# -*- coding = utf-8 -*-
# @Time : 2020/7/28 21:25
# @Author : EmperorHons
# @File : Rookie064.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-timstamp-str.html
Python 将时间戳转换为指定格式日期
"""

import time
import pysnooper


@pysnooper.snoop()
def specify_Time():
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    # print(timeArray)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    return otherStyleTime


if __name__ == '__main__':
    specify_Time()
