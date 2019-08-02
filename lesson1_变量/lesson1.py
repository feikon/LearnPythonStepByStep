"""
# Part1 变量类型
answer1 = 42                                            # int类型
answer2 = -100.0                                        # float类型
answer3 = 'zyf love zqq'                       # str类型
answer4 = [1, 2, 3, 4]                                  # list列表类型---可变，支持重新赋值
answer4[0] = 5
answer5 = (1, 2, 3, 4)                                  # tuple元组类型---不可变，不支持重新赋值
answer6 = {'zyf':'zqq', 'dongyong':('qixiannv', 'baxiannv')} # dic字典类型key-value  --可变，支持重新赋值
answer6['dongyong'] = 'baisuzhen'                       # 字典value的更新


print(answer1, answer2, answer3, answer4, answer5, answer6)
print(type(answer1), type(answer2), type(answer3),
      type(answer4), type(answer5),type(answer6))     # type函数查看变量类型


# Part2 变量类型转换
a = '9'
print(a, type(a))
b = int(a)
print(b, type(b))

# Part3 变量 命名
myDesk = 'lantingjixu'            # 小驼峰 第一个单词首字母小写，后面其他单词首字母大写。
MyDeskTop = 'Mac Air Pro'         # 大驼峰(帕斯卡) 每个单词的第一个字母都大写
my_beautiful_keyboard = 'cherry'  # 下划线命名，不推荐

"""


