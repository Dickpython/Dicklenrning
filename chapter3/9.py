# 请编写一个程序，该程序从控制台接收一个字符串，然后以相反的顺序打印它。
line_1 = input("请输入")
line_2 = []
n = 0
for i in range(0,len(line_1)):
    line_2.append(line_1[len(line_1)-i-1])
print(line_2)
