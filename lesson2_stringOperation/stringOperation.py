# -*- coding: utf-8 -*-
'''
# Created on 08-02-19 21:30
# stringOperation.py
# @author: crossfirestater@gmail.com
'''

# string1 = 'I'                           # 单引号
# print(string1, type(string1))

# string2 = "love"                        # 双引号
# print(string2, type(string2))

# string3 = """U"""                        # 双引号
# print(string3, type(string3))

# stringAddOperation = string1 + string2 + string3        # 字符串合并
# print(stringAddOperation)
# stringAddOperation2 = ' '.join(stringAddOperation).join('ABC')
# print(stringAddOperation2)

# string4 = 'I love U '                        # 字符串相乘
# string5 = string4 * 100
# print(string5)

# string6 = 'ChinaNO1'                            # 字符串切片
# print(len(string6))
# string6_C = string6[0]
# print(string6_C)
# string6_China = string6[0:5]
# print(string6_China)
# string6_NO = string6[5:7]
# print(string6_NO)
# string6_1 = string6[:5]
# print(string6_1)

# string7 = 'abc'                                 # 字符串方法
# subString7 = 'd'
# print(string7.find(subString7))

print('{} love {}'.format('I', 'U'))