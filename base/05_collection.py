# 集合相关的demo

# 使用列表
import os
import sys
import time


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


def set_test():
    set1 = {1, 2, 3, 4, 5}
    print('set1', set1)
    print('集合长度为', len(set1))
    set2 = set(range(1, 10))
    print('set2', set2)
    set3 = set((1, 2, 3, 4, 5, 6, 7))
    print(set2, set3)
    # 创建集合的推导方法
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print('set4', set4)
    # 向集合中添加元素
    set1.add(6)
    set1.add(7)
    set2.update([11, 12])
    # 从集合中删除存在的元素
    set2.discard(11)
    if 4 in set2:
        set2.remove(4)
    print(set1, set2)
    print(' pop set3', set3.pop())
    print('set3', set3)

    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


# 创建字典 它们都是 key val 形式的
def dictionary_test():
    # 创建字典
    scores = {'张三': 1, '李四': 2, '王老五': 3}
    print(scores)
    # 创建字典的构造器
    items1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压缩为字典
    item2 = dict(zip(['a', 'b', 'c'], '123'))
    # 创建推导式的字典
    item3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, item2, item3)
    # 通过key获取字典
    print(scores['张三'])
    # 遍历字典
    for key in scores:
        print(f'{key}:{scores[key]}')
    # 更新字典中的元素
    scores['张三'] = 3
    scores.update(刘八=11, 陈九=12)
    print(scores)

    if '刘八' in scores:
        print(scores['刘八'])
    print(scores.get('刘八'))
    # get可以获取值,也可以设置默认值 但不会修改源字典值
    print(scores.get('刘八', 66))
    print(scores)
    # 删除字典元素 返回删除的键
    print(scores.popitem())
    print(scores.popitem())
    print(scores)
    # 删除指定元素元素
    print(scores.pop('张三',666))
    print(scores)
    scores.clear()
    print(scores)

# 模拟跑马灯效果
def text_test():

    content = '你是干什么滴......';
    while True:
        # 如果这里执行报错(TERM environment variable not set.) 请看 https://blog.csdn.net/telltao/article/details/128393895
        os.system('clear')
        print(content)
        # 休眠 200 毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    # python中的列表
    # list_test()
    # 数组字符串分割
    # list_str_split()

    # 数组生成器
    # list_generate()

    # 元组
    # tuples_final()

    # 集合
    # set_test()

    # 字典
    #dictionary_test()
    # 模拟跑马灯效果
    text_test()
