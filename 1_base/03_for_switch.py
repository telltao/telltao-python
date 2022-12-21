"""
本章节示例的是循环语句

"""

# 计算1 ~ 100的和
def sum_num():
    # 计算 计算1~100求和
    sum = 0
    # range 会得到0~100的整数
    for x in range(101):
        sum += x
    print(sum)
    #range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
    #range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
    #range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
    #range(100, 0, -2)：可以用来产生100到1的偶数，其中 - 2 是步长，即每次数字递减的值。

    num = int(input('请输入数字'))
    while num < 10:
        print('%d 数字小于10,正在累加值' % (num))
        num+=1

        if (num > 5):
            print("数字大于5,中断循环")
            break
        continue

def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    # 计算1~100的和
    #sum_num()
    a = 100
    foo()


