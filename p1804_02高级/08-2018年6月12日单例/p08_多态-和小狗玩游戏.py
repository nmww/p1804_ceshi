#-*-coding:utf-8-*-
# 多态的举例理解
# 人和小狗做游戏
class Dog(object):
    def game(self):
        return '普通小狗，玩儿泥巴……'
class XiaoTianQuan(Dog):
    def game(self):
        return '哮天犬玩，飞到天上，玩儿泥巴&……'
class DaHuangGou(Dog):
    def game(self):
        return 'ccc，飞到天上，玩儿泥巴&……'
class Person(object):
    def play_with_dog(self, dog):   # 人想要做的事情，只是和狗玩游戏
        print('人在和 ', dog.game())
d = Dog()
p = Person()
p.play_with_dog(d)



