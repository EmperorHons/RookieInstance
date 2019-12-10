# -*- coding:utf-8 -*-
"""
https://www.runoob.com/python3/python3-leap-year.html Python 判断闰年
"""

import pysnooper


@pysnooper.snoop()
def LeapYear():
    year = int(input("输入一个年份："))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0}是闰年".format(year))  # 整百年能被4整除的是闰年
            else:
                print("{0}不是闰年".format(year))
        else:
            print("{0}是闰年".format(year))  # 非整百年能被4整除的是闰年
    else:
        print("{0}不是闰年".format(year))


if __name__ == '__main__':
    LeapYear()