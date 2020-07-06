# -*- coding = utf-8 -*-
# @Time : 2020/7/6 22:05
# @Author : EmperorHons
# @File : Rookie052.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-check-substring-present-given-string.html
Python 判断字符串是否存在子字符串
"""

import pysnooper


@pysnooper.snoop()
# find 查找
def string_Check(string, sub_str):
    # if (string.find(sub_str)) == 4:
    if (string.find(sub_str)) == -1:
        # 因为-1的意思代表没有找到字符，所以判断==-1就代表找不到
        # 4的意思是sub_str字符从那个序开始，因为b位于第五个，及序为4，所以判断4
        # https://www.cnblogs.com/Tcorner/p/9115867.html
        print("不存在")
    else:
        print("存在")


# in
def string_In(string, sub_str):
    if sub_str in string:
        print("存在")
    else:
        print("不存在")


if __name__ == '__main__':
    string = "www.baidu.com"
    sub_str = "baidu"
    print(string_Check(string, sub_str))
    print(string_In(string, sub_str))