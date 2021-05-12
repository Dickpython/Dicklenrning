# 使用给定的列表[12,24,35,24,88,120,155,88,120,155]，编写一个程序，在删除所有保留原始顺序的重复值之后，打印此列表。
#方法1
list_1 = [12,24,35,24,88,120,155,88,120,155]
list_2 = set(list_1)
print(sorted(list_2))
#方法2
def delt( n ):
    list_1 = []
    list_2 = set()
    for x in n:
        if x not in list_2:
            list_2.add( x )
            list_1.append(x)
    return list_1
n = [12,24,35,24,88,120,155,88,120,155]
print(delt(n))
