#-*-coding:utf-8-*-

# 植物大战僵尸2

# 单行注释
'''多行注释'''

class Zombie:
    def __init__(self, name, ph, color):
        '''僵尸类'''
        self.name = name
        self.ph = ph
        self.color = color
    def __str__(self):
        s = self.name + " 僵尸 出现了，很闪闪着  " + self.color + ' 的光芒 ， 充满 ' + self.ph +' 血量，向你飞奔而来。'
        return s
    def eat(self):
        '''这是一个吃的方法'''
        print ("%s 僵尸正在努力啃咬目标……"% self.name)
    def run(self):
        print ('%s 僵尸奔跑起来了……'% self.name)

zb01 = Zombie('普通', '100', '灰色')
zb02 = Zombie('跳跳', '80', '红色')
zb01.eat()
print(zb01)
print(zb02)






