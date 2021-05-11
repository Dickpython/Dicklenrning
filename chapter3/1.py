# 编写一个程序来计算输入中单词的频率。在按字母数字顺序对键进行排序后，应输出输出。
# 如，输入：New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 输出：
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
line_1 = {}
str_1 = input("请输入")
for i in str_1.split():
    line_1[i] = line_1.get(i , 0) + 1
x = sorted(line_1.keys())

for y in x:
    print("%s : %d" % (y,line_1[y]))
