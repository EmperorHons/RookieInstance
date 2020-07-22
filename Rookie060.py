# -*- coding = utf-8 -*-
# @Time : 2020/7/22 22:52
# @Author : EmperorHons
# @File : Rookie060.py
# @Software : PyCharm
"""
https://www.runoob.com/python3/python-remove-a-key-from-dictionary.html
Python 移除字典键值(key/value)对
"""

test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# 第一种方法 del 删除
del test_dict['Zhihu']
print(test_dict)

# 第二种方法 pop 删除
removed_value = test_dict.pop('Runoob')
print(test_dict)
print("移除的 key 对应的 value 为 : " + str(removed_value))

# 第三种方法 items() 移除
new_dict = {key: val for key, val in test_dict.items() if key != 'Google'}
print(new_dict)