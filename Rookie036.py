# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python-simplestopwatch.html
Python 实现秒表功能
"""

import time


print('按下回车开始计时，按下Ctrl + c 停止计时')

while True:

    input("")
    start_time = time.time()
    print('开始', start_time)
    try:
        while True:
            print('计时: ', round(time.time() - start_time, 0), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        end_time = time.time()
        print('总共的时间为:', round(end_time - start_time, 2), 'secs')
        break
