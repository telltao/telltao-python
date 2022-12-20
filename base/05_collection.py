# 集合相关的demo

# 使用列表
import sys


def list_test():
    list = [1, 2, 3, 4]
    print(list)  # {1, 2, 3, 4}
    list2 = ['hello'] * 3
    print(list2)
    print('长度为 %d' % len(list))
    print('取下标 list 第一个值为:%d' % list[0])
    print('取下标 list 第一个值为:%d,第二个值为%d' % (list[0], list[1]))
    print('取下标 list 最后一个值为:%d' % list[len(list) - 1])
    print('取下标 list 最后一个值为:%d' % list[-1])

    # 循环遍历元素
    for index in range(len(list)):
        print('循环输出 list集合的值%d' % list[index])
    for elem in list:
        print('通过for遍历list集合的值%d' % elem)
    for index, elem, in enumerate(list):
        # print(index, elem)
        print('通过 enumerate函数遍历输出值 下标:%d,值为:%d' % (index, elem))
    # 在末尾拼接数据
    list.append(5)
    # 在第一个里插入数据
    list.insert(1, 55)
    # 合并两个列表
    # list.extend([1000, 2000])
    list += [1000, 2000]
    print(list)
    print(len(list))
    # 如果值包含3
    if 3 in list:
        list.remove(3)
    if 123 in list:
        list.remove(123)
    # 从指定位置删除数据  第一个和最后一个
    list.pop(0)
    list.pop(len(list) - 1)
    # 清空列表元素
    list.clear()
    print(list)


# list的切片
def list_str_split():
    list = ['aa', 'dd', 'hh', 'ff', 'bb']
    list.sort()
    print(list)
    # 反向排序 sorted函数返回列表排序后的拷贝不会修改传入的列表
    list2 = sorted(list, reverse=True)
    print(list2)
    list4 = sorted(list, key=len)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list.sort(reverse=True)
    print(list)


def list_generate():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


# 元组是不可变的数据
def tuples_final():
    """
    元组中的元素是无法修改的，事实上我们在项目中尤其是多线程环境（后面会讲到）中可能更喜欢使用的是那些不变对象（
    一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的对象更加容易维护；
    另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。
    一个不变对象可以方便的被共享访问）。所以结论就是：如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。

    元组在创建时间和占用的空间上面都优于列表。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和列表各自占用了多少内存空间，这个很容易做到。
    我们也可以在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间，下图是我的macOS系统上测试的结果。
    :return:
    """
    # 定义元组
    t = ('张三', 38, True, '北京')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '李四'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('李四', 20, True, '河北')
    print(t)
    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '张三丰'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)

if __name__ == '__main__':
    # python中的列表
    # list_test()
    # 数组字符串分割
    # list_str_split()

    # 数组生成器
    # list_generate()

    # 元组
    tuples_final()
