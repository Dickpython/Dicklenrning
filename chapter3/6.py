# 请编写一个程序以生成所有句子，其中主语位于[“ I”，“ You”]中，动词位于[“ Play”，“ Love”]中，而宾语位于[“ Hockey”，“ Football”]中。
ZY = ["I","You"]
DC = ["Play","Love"]
BY = ["Hockey","Football"]
for i in ZY:
    for j in DC:
        for x in BY:
            print("{} {} {}".format(i,j,x))
