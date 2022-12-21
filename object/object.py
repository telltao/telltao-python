"""
主要讲述的是面向对象
    类中的方法 如果以 __开头 则表示是私有
"""
from abc import abstractmethod
from time import localtime, time


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)

    # 将方法设置为私有的 直接以两个下划线开头即可

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


class Test1:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


# 一个具有get set方法的人类
class Person(object):
    # 限定只能绑定某个对象
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 18:
            print('%s正在玩儿跳棋' % self.name)
        else:
            print('%s正在工作' % self.name)

    @staticmethod
    def is_valid(age):
        if (age < 18):
            print("静态方法: 你还未成年哦")

    @classmethod
    def now_time(cls):
        ctime = localtime(time())
        return ctime

    @abstractmethod
    def make_voice(self):
        """我会说话"""
        pass

class Teacher(Person):

    def play(self):
        if (self.age < 20):
            print('这个老师现在是实习阶段,年龄小于20')
        else:
            print('这个老师年龄大于20,属于正式工')

    def make_voice(self):
        print('抽象方法重写,我是专业讲课的老师')


if __name__ == '__main__':
    student = Student('张三', 12)
    student.study('休息会再学')
    student.watch_movie()

    print("-------------")
    # 创建一个私有的类,
    test = Test('我')
    # test.__bar() 报错,因为这个方法是私有的
    test1 = Test1("你好")
    # test1._Test__bar()
    print("-------------")
    # 创建一个对象 并配置 get,set方法
    person = Person('张三', 15)
    person.play()
    person.age = 22
    person.play()
    # 直接调用静态方法
    Person.is_valid(15)
    time = Person.now_time()
    print('直接调用类方法,当前时间为', time)
    print("-----开始执行重写关系--------")
    teacher1 = Teacher('赵老八', 25)
    teacher1.play()
    teacher1.is_valid(15)
    # 子类重写父类的抽象方法  这就是多态
    teacher1.make_voice()
