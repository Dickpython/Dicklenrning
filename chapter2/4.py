# 编写一个接受句子并计算字母和数字数量的程序。
# 假设将以下输入提供给程序：
#       hello world! 123
# 输出应为：
#       LETTERS 10
#       DIGITS 3
s = input("请输入任意字母和数字")
count = {"letters": 0,"digits": 0}
for i in s:
    if i.isalpha():
        count["letters"] += 1
    elif i.isdigit():
        count["digits"] += 1
    else :
        pass
print("LETTERS:",count["letters"])
print("DIGITS:",count["digits"])
