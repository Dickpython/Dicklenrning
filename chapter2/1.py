# 编写一个程序，该程序接受一系列由空格分隔的单词作为输入，并在删除所有重复的单词并将其按字母数字顺序排序后打印这些单词。
def none(line):
    return line and line.strip()
line_1 = set(list(filter(none,input("请随意输入字符"))))
print(sorted(line_1))
