# -*- coding:utf-8 -*-
"""
https://www.runoob.com/python3/python3-celsius-fahrenheit.html  Python 摄氏温度转华氏温度
"""

# 输入摄氏温度
celsius = float(input('输入摄氏温度： '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))