#-*-coding:utf-8-*-
# 单例模式
class Car(object):
    __instace = None  # 用于保存实例化的对象
    def __init__(self, name):
        self.name = name
        print('-----__init__方法被调用------')
    def __new__(cls, *k):
        print("--__new__方法被调用------")
        if cls.__instace == None:
            cls.__instace = object.__new__(cls)
        return cls.__instace

c1 = Car('c1')
c2 = Car('c2')
c3 = Car('c3')
c4 = Car('c4')
print(id(c1))
print(id(c2))
print(id(c3))
print(id(c4))

