# 编写一个程序，该程序根据来自控制台输入的交易日志来计算银行帐户的净额。
#    D表示存款，W表示提款。
#    如：

#    ```
#    D 300
#    D 300
#    W 200
#    D 100
#    ```

# ​       输出应为：500
num = 0
while True:
    s = input("请输入存取款情况，D为存款，W为取款")
    if not s:
        break
    s_1 = s.split(" ")
    action = s_1[0]
    value = int(s_1[1])
    if action == "D":
        num += value
    elif action == "W":
        num -= value
    else:
        pass
print(num)
