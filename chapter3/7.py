# 通过使用列表理解，请编写一个程序来删除[12,24,35,70,88,120,155]中的第0、4、5个数字，然后打印列表。
list_1 = [12,24,35,70,88,120,155]
list_2 = [x for (i,x) in enumerate(list_1) if i not in (0,4,5)]
print(list_2)
