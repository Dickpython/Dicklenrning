# 请编写程序以打印"1 + 1"的运行100次，所花的时间
import timeit
time_1 = timeit.timeit(stmt ='1+1',number=100)
print(time_1)
