# 编写一个程序来按升序对（名称，年龄，分数）元组进行排序，其中名称是字符串，年龄和分数是数字。元组由控制台输入。排序标准是：

#    ```
#    Tom,19,80
#    John,20,90
#    Jony,17,91
#    Jony,17,93
#    Json,21,85
#    ```

# ​      输出应为：
# ​      [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# _*_ coding: utf-8 _*_
from operator import itemgetter
line1 = []
while True:
    s = input("请输入：")
    if not s:
        break
    line1.append(tuple(s.split(",")))
print(sorted(line1,key = itemgetter(0,1,2)))
