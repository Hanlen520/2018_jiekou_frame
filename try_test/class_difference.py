"""
#1.静态方法
class ClassA1():
    @staticmethod
    def func_a():
        print("hello world")

if __name__ == '__main__':
    ClassA1.func_a()
    # 也可以使用实例调用,但是不会将实例作为参数传入静态方法
    ca=ClassA1
    ca.func_a()
"""
"""
#2.类方法
class ClassA():
    @classmethod
    def func_a(cls):
        print(type(cls),cls)

#类调用
ClassA.func_a()

#实例调用
ca=ClassA()
ca.func_a()
"""

"""
#3.类继承，如果存在类的继承，那类方法获取的类是类树上最底层的类。

class BaseA():

    @classmethod
    def func_a(cls):
        print(type(cls), cls)

class BaseB(object):
    pass

class ClassA(BaseA, BaseB):
    pass

if __name__ == '__main__':

    ClassA.func_a()

    ca = ClassA()
    ca.func_a()
"""

"""
#4.实例方法
class ClassA(object):

    def func_a(self):
        print('Hello Python')

if __name__ == '__main__':
    # 使用实例调用实例方法
    ca = ClassA()
    ca.func_a()
    # 如果使用类直接调用实例方法,需要显式地将实例作为参数传入
    ClassA.func_a(ca)
"""