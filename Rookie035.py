# -*- coding: utf-8 -*-
"""
https://www.runoob.com/python3/python-five-fish.html
Python 五人分鱼
"""
import pysnooper


@pysnooper.snoop('log.md')
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


if __name__ == '__main__':
    main()
