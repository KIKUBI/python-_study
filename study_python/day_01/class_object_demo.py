# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      class_object_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/2 11:30
# Description:
# 
# ---------------------------------------------------------------------------


"""
    面向对象：面向对象是一种编程思维，把解决的问题抽象成一个一个类，类就是一个模板，类中具有事务的静态特征(属性)和动态特征(方法)，
            可以根据类，创建多个对象，对象具有事务具体静态特征和具体的动态特征(对象具有类中的静态特征和动态特征)。

"""
# 类的声明
"""
class 类名:   # 类名的首字母尽量大写 
    定义属性(静态特征)
    
    # 定义动态特征
    def 方法名():
        方法体

"""
# 对象的创建
"""
对象名 = 类名()

# 对象调用类中的属性和方法的格式：对象名.属性名   /   对项名.方法名()
"""
"""
    cls: 表示类本身
    self: 表示类对象本身
    注意：类外和类里面，类对象可以访问类中任何属性和任何方法。
         在类外和类里，类名和类本身只能访问类中类属性、类方法和静态方法。
"""
# 属性
"""
    对象属性/实例属性：所有类对象自己的具体静态特征，在有self的地方可以定义对象属性。
    类属性：所有的类对象公共的静态特征
"""
# 方法：
"""
    对象方法/实例方法：对象方法有个必须形参为self，self必须在方法的第一个形参。在调用方法时，不用给self传参。
                对象方法能够访问类中任何属性和任何方法
                
                构造方法：__init__(self): 初始化类对象，构造方法在创建对象时，默认执行
                        在构造方法中一般用例初始化类对象的属性和方法
                析构方法：__del__(self): 类对象使用完之后，默认执行，一般是用例回收资源使用。---慎用
                
    类方法：需要使用装饰器@classmethod装饰的方法，就为类方法，类方法有一个必须形参cls，cls必须在类方法中作为第一个形参，在调用类方法是cls不用传参。
            类方法中一般可以定义类属性。
    
    静态方法：需要使用装饰器@staticmethod装饰的方法，就为类方法,静态方法没有必须形参.静态方法没法调用类中的任何属性和方法。
    
    注意：在类外可以定义对象的属性，但是不要定义。

"""
"""
    装饰器：功能在不改变源代码的情况下，丰富被装饰器对象的功能。
"""

'''
class Student:
    address = "蓉华"   # 类属性

    def study(self, stu_name):
        # print(self)
        # print(self.address)
        age = 18
        self.name = stu_name   # 对象属性
        print("学习方法")

    def sleep(self):
        self.study("李四")
        print(f"{self.name}想睡觉, 他现在有：{self.age}岁，在：{self.address}学习")


zhang_san = Student()   # 创建类的对象
'''
'''
print(zhang_san, type(zhang_san))


print(zhang_san.address)   # 访问类中的属性
# zhang_san.study("张三")           # 访问类中的方法


zhang_san.sleep()
print(zhang_san.name)

print("-"*100)
print(Student.address)
'''

# zhang_san.age = 19   # 慎用
# zhang_san.sleep()

'''
class Demo:
    type = "类属性"

    def __init__(self, stu_name, stu_age):
        self.name = stu_name
        self.age = stu_age
        print("构造方法")

    def __del__(self):
        print("析构方法")

    @classmethod
    def class_method1(cls):
        print("==========类方法1========")

    @classmethod
    def class_method(cls):
        print("cls为：", cls)
        print("类方法")
        cls.class_method1()
        print(f"=========={cls.type}===========")

    def func1(self):
        print(f"func1方法， 访问对象属性：{self.name}, {self.age}")

    def func2(self):
        print("-"*100)
        print("func2方法")
        self.class_method()
        print(self.type)
        print("-" * 100)


d = Demo("李四", 19)
# d.func1()

# d1 = Demo("李二", 20)
# d1.func1()

d.class_method()
# print(Demo)
print(Demo.type)
Demo.class_method()
'''


class Demo1:

    class_property = "类属性"

    def __init__(self):
        self.class_method()

    @staticmethod
    def static_method(name, age):
        print("静态方法", name, age)
        # static_method()

    def object_method(self):
        self.variable = "对象属性"
        self.static_method()
        print(self.age)

    @classmethod
    def class_method(cls):
        cls.property = "类属性"
        print("类方法")


print(Demo1.class_property)

Demo1.class_method()
Demo1.static_method("tom", 18)