def inputqwe():
    """
    使用input()函数获取键盘输入(字符串)
    使用int()函数将输入的字符串转换成整数
    使用print()函数输出带占位符的字符串

    Version: 0.1
    Author: 骆昊
    """
    a = int(input('a = '))
    b = int(input('b = '))
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))


def equals():
    """
    比较运算符和逻辑运算符的使用

    Version: 0.1
    Author: 骆昊
    """
    flag0 = 1 == 1
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not (1 != 2)
    print('flag0 =', flag0)  # flag0 = True
    print('flag1 =', flag1)  # flag1 = True
    print('flag2 =', flag2)  # flag2 = False
    print('flag3 =', flag3)  # flag3 = False
    print('flag4 =', flag4)  # flag4 = True
    print('flag5 =', flag5)  # flag5 = False


def fahrenheit_to_celsius():
    """
    将华摄度转换为摄氏度 转换公式 $C=(F - 32) / 1.8。

    :return:
    """
    a = int(input('请输入华氏度 '))
    c = (a - 32) / 1.8
    print("华氏度:%f,摄氏度:%f" % (a, c))
    print('%.1f华氏度 = %.1f摄氏度' % (a, c))
    """
    说明：在使用print函数输出时，也可以对字符串内容进行格式化处理，上面print函数中的字符串%.1f是一个占位符，
    稍后会由一个float类型的变量值替换掉它。同理，如果字符串中有%d，后面可以用一个int类型的变量值替换掉它，而%s会被字符串的值替换掉。
    除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，其中{f:.1f}和{c:.1f}可以先看成是{f}和{c}，
    表示输出时会用变量f和变量c的值替换掉这两个占位符，后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字。
    """


def leap_year():
    """
    根据输入的年份计算是否是闰年
    :return:
    """
    year = int(input('请输入年份: '))

    # 闰年的规则 能被4整除,并且不是100的倍数,或是400的倍数
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    if is_leap:
        print("%d年是闰年" % (year))
    elif is_leap:
        print("%d年是闰年 else if " % (year))
    else:
        print("%d年不是闰年" % (year))


def circumference():
    """
    输入半径计算圆的周长和面积
    :return:
    """
    radius = float(input('请输入圆的半径:'))
    # 圆的周长  C=2πr
    perimeter = 2 * 3.1416 * radius
    # 面积 π乘以r的平方
    area = 3.1416 * radius * radius
    print('圆的周长%.2f' % (perimeter))
    print('圆的面积%.2f' % (area))


if __name__ == '__main__':
    # a = 100
    # b = 12.345
    # c = 1 + 5j
    # d = 'hello, world'
    # e = True
    # print(type(a))  # <class 'int'>
    # print(type(b))  # <class 'float'>
    # print(type(c))  # <class 'complex'>
    # print(type(d))  # <class 'str'>
    # print(type(e))  # <class 'bool'>

    # inputqwe();
    # equals();
    # 摄氏度转华氏度
    # fahrenheit_to_celsius();
    # 输入圆的半径并计算周长和面积
    # circumference();
    # 判断年份是不是闰年
    leap_year();
