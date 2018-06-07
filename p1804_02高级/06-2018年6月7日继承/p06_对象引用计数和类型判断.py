#-*-coding:utf-8-*-

# 对象的引用数量查询
import sys

class People:
    def __init__(self, name, salary):
        self.__name = name   # 声明了 这个属性 为 类私有
        self.salary = salary
class Worder:
    def __init__(self, name, salary):
        self.__name = name   # 声明了 这个属性 为 类私有
        self.salary = salary

xiaohua01 = People('小花01',5000)
xiaohua02 = xiaohua01
xiaohua03 = xiaohua01
print( sys.getrefcount(xiaohua01))  # 对象被引用了多少次，数量显示要比实际引用次数 多1
print(isinstance(xiaohua03, People)) # True ; Flase  查询对象是否属于 指定的类
