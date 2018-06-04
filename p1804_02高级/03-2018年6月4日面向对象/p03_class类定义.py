#-*-coding:utf-8-*-

# 怎么定义一个类
# 名片管理系统  ：   名片类（姓名、公司、邮箱； 增、删、改、查）     **人的名片
''' 类： 的三个关键 要素：  类名称、属性、行为/方法'''

class People:
    def eat(self):  # 行为，方法
        print('正在吃午餐…… ')
    def word(self):
        print('正在努力工作……')

xiaoming = People()  # 调用人类 创建 具体的 xiaoming对象
xiaoming.age = 20     # 给对象 设置 属性
xiaoming.name = 'xiaoming'  # 给对象 设置 属性
xiaoming.eat()         # 具体对象 执行 继承的能力
xiaoming.word()




