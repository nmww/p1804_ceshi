#-*-coding:utf-8-*-

#继承

class Animal:
    def __init__(self):
        self.legs = 4
        self.weiba = 1
    def eat(self):
        print ('动物天生吃东西能力；')
    def drink(self):
        print('动物天生  喝水 的能力；')
    def sleep(self):
        print ('倒头就睡的能力。')

class Dog(Animal):
    def jiao(self):
        print('小狗 旺旺旺旺 叫')

class Shapi(Dog):
    pass

gou = Dog()
print ('小狗天生 '+str(gou.legs) +" 条腿。")

xp = Shapi()
xp.jiao()
xp.sleep()