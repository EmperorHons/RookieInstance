# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-calendar.html    Python 生成日历
"""
import calendar


yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))
