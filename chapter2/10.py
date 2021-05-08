# 用生成器定义一个类，该生成器可以迭代在给定范围0和n之间可以被7整除的数字。
# _*_ coding: utf-8 _*_
def fib(n):
    a = 0
    while a < n:
        b = a
        a += 1
        if b % 7 == 0:
            yield b
for a in fib(int(input("请输入数字："))):
    print(a)
