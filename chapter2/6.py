# 编写一个程序，以给定的数字作为a的值来计算a + aa + aaa + aaaa的值。
x = input("请输入一个数字")
n1 = int(x)
n2 = int(n1 * 10 + n1)
n3 = int(n2 * 10 + n1)
n4 = int(n3 * 10 + n1)
print(n1+n2+n3+n4)
