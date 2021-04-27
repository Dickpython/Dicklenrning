# 编写一个接受句子的程序，并计算大写字母和小写字母的数量。
s = input("请输入句子")
count = {"lettersH": 0,"lettersL": 0}
for i in s:
    if i.isupper():
        count["lettersH"] += 1
    elif i.islower():
        count["lettersL"] += 1
    else :
        pass
print("其中大写字母：",count["lettersH"])
print("其中小写字母：",count["lettersL"])
