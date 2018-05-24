# 多变量赋值
x, y, z = 10, 15, 20
x, y = z, x
print("x: %d y: %d" % (x, y))

# 使用input等待用户输入

# msg = input("请输入内容")
# print("内容是: " + msg)

# 查看变量类型
print(type("字符"))
print(type(5))
print(type(4.15151))

# 基本语句
# x = 0
# z = 1
if (x > y):
    print("x")
elif (y > z):
    print("y")
else:
    print("z")

for letter in range(1, 8, 2):
    print("letter is " + str(letter))

numbers = [1, 2, 3, 4]
while len(numbers) > 0:
    number = numbers.pop()
    if number < 2:
        print(" pass 的语句 ")
        pass

    print("number is " + str(number))

import random

# 随机数
for item in range(1, 4):
    print("随机数：" + str(random.randint(1, 10)))

# format

info = "姓名：{} 性别 {}".format("橡胶人", "男")
print(info)

# 程序计时器
import datetime
import time

# 开始记时
startTime = datetime.datetime.now()
# time.sleep(1)

# 结束记时
endTime = datetime.datetime.now()
print("结束时间: " + str(endTime - startTime))

# 列表
list1 = [False, int(222), "wahahah"]
del list1[list1.__len__() - 1]
list1.append("新的")
list1.insert(0, 0)
list1.reverse()
print(list1)

# 元祖
list2 = (1, 3, 4)
print(list2.__len__())

# 字典
dict = {}
dict["key1"] = "value1"
dict["key2"] = 4
print(dict)
print("keys is " + str(dict.keys()))
print("keys is " + str(dict.items()))


# 函数
def fun1():
    return "第一个函数"


print(fun1())


# 缺省函数,不定参数 , 默认10岁
def showToInfo(age=10, *name):
    if name.__len__() > 0:
        print("name is {} age is {}".format(name, age))
    else:
        print("没有名字 只有年龄 " + str(age))


showToInfo()
showToInfo(18)
showToInfo(18, "我最帅", "名字是")


# *元祖与解包 *代表是元祖, ** 代表是字典
def accept(*s):
    print(s)
    print(sum(s))


d_list = (0, 1, 2, 3, 7.5)
print(sum(d_list))
# accept(list) 这样会报错
accept(*d_list)

# import First
from First import printCat

printCat()

from First import printDog

printDog()



