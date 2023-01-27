
# -*- coding:utf-8 -*-

# 类函数 和 静态函数

class People(object):
    __seats = 10  # 总计座位数
    __seat_type = 1  # 座位类型

    def __init__(self, name, age):
        # 调用父类的初始化函数
        super(People, self).__init__()
        # 初始化当前类对象的一些属性
        self.name = name
        self.age = age

    @property
    def seats(self):  # 商品总价
        return self.__seats

    @classmethod
    def change_seats(cls, n, t):
        People.__seats = n
        cls.__seat_type = t
        print(f'总共{cls.__seats} seats')

    # 对象函数，只能由对象调用
    def eat(self):
        print(f'{self.name}该吃饭了...')

    # 类函数
    # 装饰器是以@开头，@结构的称之为语法糖，装饰器的作用主要是给一些现有的函数增加一些额外的功能
    @classmethod
    def work(cls, time):
        # cls  class 如果是类调用该函数，cls指的就是这个类
        # 如果是对象调用该函数，cls指的就是这个对象的类型
        print(cls)
        print(time)

    @classmethod
    def sleep(cls):
        print('每一个类函数前都需要添加装饰器')

    # 静态函数
    # @staticmethod 描述的函数称为静态函数，静态函数可以由类和对象调用，函数中没有隐形参数
    @staticmethod
    def run(time):
        print('跑步%s分钟' % time)

    def take_(self, n):
        People.__seats = People.__seats - n
        print(f'{self.name} take {n} seats')

    def return_(self, n):
        People.__seats = People.__seats + n
        print(f'{self.name} return {n} seats')


# 对象函数只能由对象调用
# 类函数由类调用，也可以用对象调用
People.work(10)
p1 = People('张三', 22)
p1.work(20)

People.run(10)
p1.run(20)

print(p1.seats)  # 属性，不需要加括号
People.change_seats(20, 2)
print('现有座位:', p1.seats)

p1.take_(2)
p1.return_(1)
print('剩余座位:', p1.seats)

p2 = People('李四', 33)
p2.take_(5)
print('剩余座位:', p1.seats)


