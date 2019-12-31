# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-get-yesterday.html
Python 获取昨天日期
"""

import datetime
import pysnooper


@pysnooper.snoop()
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


print(getYesterday())
