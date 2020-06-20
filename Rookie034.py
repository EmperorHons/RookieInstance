# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python-joseph-life-dead-game.html
Python 约瑟夫生者死者小游戏
"""
import pysnooper


@pysnooper.snoop('txt.md')
def safe():
    people = {}

    for x in range(1, 31):
        people[x] = 1
    check = 0  # 计数，到9，编号为i的人下船
    i = 1   # 编号
    j = 0   # 下船的人数
    while i <= 31:
        if i == 31:
            i = 1
        elif j == 15:
            break
        else:
            if people[i] == 0:
                i += 1
                continue
            else:
                check += 1
                if check == 9:
                    people[i] = 0
                    check = 0
                    print("{}号下船了".format(i))
                    j += 1
                else:
                    i += 1
                    continue


if __name__ == '__main__':
    safe()
