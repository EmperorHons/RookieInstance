# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-check-string.html  Python 字符串判断
"""

from termcolor import colored

print('测试实例')
str = 'github.com'

print(str.isalnum())  # 判断所有字符都是数字或字母
print(str.isalpha())  # 判断所有字符都是字母
print(str.isdigit())  # 判断所有字符都是数字
print(str.islower())  # 判断所有字符都是小写
print(str.isupper())  # 判断所有字符都是大写
print(str.istitle())  # 判断所有单词都是首字母大写，像标题
print(str.isspace())  # 判断所有字符都是空白字符、\t、\n、\r

print(colored("-" * 20, 'green'))