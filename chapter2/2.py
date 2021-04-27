# 编写一个程序，该程序接受以逗号分隔的4位二进制数字序列作为输入，然后检查它们是否可被5整除。被5整除的数字将以逗号分隔的顺序打印。
line_2 = []
line_00 = [x for x in input("请输入需要打印的二进制数").split(",")]
for i in line_00:
    ten = int(i,2)
    if ten % 5 == 0:
        line_2.append(i)
print(",".join(line_2))
