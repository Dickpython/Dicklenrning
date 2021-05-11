# 当控制台输入n时，请使用生成器编写一个程序，以逗号分隔的形式打印0到n之间的偶数。
line_1 = []
def fib(n):
    a = 0
    while a <= n:
        b = a
        a += 1
        if b % 2 == 0:
            yield b
for a in fib(int(input("请输入数字："))):
    c = str(a)
    line_1.append(c)
print(",".join(line_1))
