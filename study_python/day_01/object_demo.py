# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      object_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/5 10:49
# Description:
# 
# ---------------------------------------------------------------------------
"""
    面向对象：面向对象是一种编程思想，把解决的问题抽象成一个一个类，类中具有事务的属性和方法，类就是一个模板
            可以根据这个模板创建出多个对象，每个对象是具体的事物，具体具体的属性和具体的方法。
            对象具体类的所有属性和方法。
"""
"""

class 类名:
    # 公共的静态特性
    类属性 = 值
    
    def __init(self[, 形参])：
        # self: 类对象本身
        # 可以调用类中任何属性和任何方法
        # 对象具体的静态特征
        self.对象属性 = 值
        
    def object_method(self[, 形参]):
        # 对象具体的动态特征
        
    @classmethod
    def class_method(cls[, 形参])：
        # cls: 类本身
        # 类方法只能调用类中的类属性和类方法、静态方法
        # 功能的动态特征
        # 定义公共的静态特征

    @staticmethod
    def static_method([形参]):
        # 功能的动态特征
        # 静态方法不能调用类中任何属性和任何方法
        # 该方法没有使用类属性和对象属性时，可以定义为静态方法。
"""
"""
    面向对象的特点：
        封装：属性和方法的访问权限的控制----有前置的封装为类，没有前置的封装为函数
        继承：类可以继承一个类或多个类型
                在继承时，构造方法会出现的以下情况：
                    1：子类和父类同时存在构造方法,子类创建对象时，默认调用自己的构造方法。---官方推荐在子类的构造方法中使用super调用父类的构造方法。
                    2：子类没有构造方法，父类有构造方法，子类创建对象时，默认调用父类的构造方法。
                    3：子类和父类同时不存在构造方法,子类创建对象时，python解释器会给子类和父类默认创建一个构造构造方法，子类创建对象时，默认调用父类的构造方法
                    
                super的使用场景：父类和子类的类属性和方法名称相同时，如果子类需要使用父类的类属性和方法时，可以在子类中使用super调用父类的类属性和方法。
                super的功能：使用子类对象调用父类的类属性和方法，在父类方法中的self为子类对象。
                如果子类和父类的方法或属性没有重名时，直接在子类使用self调用父类的属性或方法
                
                多继承时，需要使用__mro__来查看继承的顺序。
        多态:--python中是没有多态的。

"""

'''
class Student:
    # 公共的属性
    addr = "成都"

    # 具体的属性
    def __init__(self, name, age):
        # 创建对象属性
        self.name = name
        self.age = age

    # 具体的动态特征
    def study(self):
        print(f"{self.name}，今年：{self.age}岁，在{self.addr}学习")

    # 公共的动态特征
    @classmethod
    def study_content(cls):
        print(f"在{cls.addr}学习测试")


stu = Student("张三", 18)
stu.study_content()
stu.study()
'''


'''
class Basic:
    class_property = "basic中类属性"

    def __init__(self, name):
        self.object_property = "basic中实例属性"
        self.name = name

    def object_method(self):
        print("basic中实例方法")

    @classmethod
    def class_method(cls):
        print("basic中类方法")

    @staticmethod
    def static_method():
        print("basic中静态方法")


class ChildClass(Basic):
    class_property = "childClass类中的类属性"   # 如果子类和父类类属性名称相同，子类会调用自己的类属性

    def __init__(self):
        self.object_property = "childClass类中的对象属性"    # 如果子类和父类对象属性名称相同，子类会调用自己的对象属性
        super().__init__(name="tom")

    def object_method(self):
        print("childClass中实例方法")

    @classmethod
    def class_method(cls):
        # super(类名, 对象).父类方法()
        super(cls, cls()).class_method()

    @staticmethod
    def static_method():
        super(ChildClass, ChildClass()).static_method()

    def object_method2(self):
        # 需要调用父类的方法，需要使用super进行调用，super的功能：使用子类对象调用父类的方法或类型
        print("-"*100)
        super().object_method()
        print(super().class_property)
        # print(super().object_property)
        print(self.object_property)


child = ChildClass()
# print(child.class_property)
# print(child.object_property)
# child.object_method()
# child.object_method2()
# child.class_method()
child.static_method()
'''

'''
class A:
    def demo(self):
        print("A类的demo方法")


class B(A):
    def demo(self):
        print("B类的demo方法")
        super(C, self).demo()


class C(A):
    def demo(self):
        print("C类的demo方法")


class D(B, C):
    pass


# c = C()
# c.demo()
# super(B, c).demo()   # 使用父类的名称调用父类的父类的方法。


d = D()


# __mro__：查看类的继承顺序
print(D.__mro__)

# super(B, d).demo()  # 调用C类
# super(C, d).demo()  # 调用A类
# super(D, d).demo()  # 调用B类
# d.demo()            # 调用D类自己的demo


super(D, d).demo()
'''

'''
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print(f"A类中add方法中的self为：{self}")
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print(f"B类中add方法中的self为：{self}")
        super().add(m)
        self.n += 3


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print(f"C类中add方法中的self为：{self}")
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print(f"D类中add方法中的self为：{self}")
        super().add(m)
        self.n += 5


d = D()
d.add(5)
print(d.n)
'''


"""
class Demo:
    def func1(self):
        print("func1--------1")

    def func1(self):
        print("func1--------2")
"""
'''
class Demo:

    def func1(self):
        print("func1==========2")
        yield 1
        yield 2

    def func2(self, n):
        if n == 1:
            return 1
        else:
            return self.func2(n-1)+n

demo = Demo
d = demo()
gen = d.func1()
print(gen, type(gen))


res = d.func2(5)
print(res)
'''


class Animal:
    def sleep(self):
        pass


class Cat(Animal):
    def sleep(self):
        print("猫在睡觉")


class Dog(Animal):
    def sleep(self):
        print("狗在睡觉")


def animal_sleep(animal):
    animal.sleep()


cat = Cat()
dog = Dog()

animal_sleep(cat)
animal_sleep(dog)