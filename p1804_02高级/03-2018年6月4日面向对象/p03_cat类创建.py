#-*-coding:utf-8-*-
# cat 猫

#  类型的名称  类的方法
class Cat:
    def eat(self):
        print("%s 在吃鱼……"% self.name)
    def drink(self):
        print('%s 在和啤酒……'% self.name)
    def introduce(self):
        print('我的名字是%s, 我今年%d岁了。' % (self.name, self.age))
#------------以上部分，是对类的定义（抽象）

tom = Cat()   # 用类 创建一个对象 tom
tom.age = 60  # tom对象 设置 属性
tom.color = 'blue' #
tom.name = 'tom'
tom.introduce()
tom.eat()

lanmao = Cat()
lanmao.name = '蓝猫'
lanmao.age = 24
lanmao.color = 'red'
lanmao.introduce()
lanmao.eat()









