# -*- coding = utf-8 -*-
# @Time : 2020/7/9 22:33
# @Author : EmperorHons
# @File : Rookie055.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-execute-string-code.html
Python 将字符串作为代码执行
给定一个字符串代码，然后使用 exec() 来执行字符串代码。
"""

import pysnooper


@pysnooper.snoop()
def exec_Code():
    loc = """
def find_Len(string):
    i = 0
    while string[i:]:
        # print(i)
        # print(string[i:])
        i += 1
    return i
    
print(find_Len("stringNumber"))
"""
    exec(loc)


if __name__ == '__main__':
    exec_Code()
