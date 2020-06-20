# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python3-file-io.html  Python 文件 IO
"""
from termcolor import colored

with open("text.txt", "wt") as out_file:
    out_file.write("第一句话\n换行写第二句话")


with open("text.txt", "rt") as in_file:
    text = in_file.read()

print(colored(text, 'green'))
