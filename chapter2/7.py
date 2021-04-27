# 使用列表推导对列表中的每个奇数取平方。该列表由逗号分隔的数字序列输入。
# 如：1,2,3,4,5,6,7,8,9
# 输出：1,9,25,49,81
line_1 = []
line_j =[x for x in input("请输入数列").split(",")] 
for i in line_j:
    line_2 = int(i)
    if line_2 % 2 == 1:
        s = str(line_2*line_2)
        line_1.append(s)
print(",".join(line_1))
