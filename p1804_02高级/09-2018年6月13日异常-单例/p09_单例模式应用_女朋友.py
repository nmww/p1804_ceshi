#-*-coding:utf-8-*-

'''
练习：  单例模式
	1. 创建一个女朋友对象；继承object父类
	2. 实现女朋友的单例
	3. 实现女朋友名字的单例
	4. 创建两个女朋友，看看是否出现两个女友。
'''
class GirlFriend(object):
    __girl = None
    __only_you = False
    def __init__(self, name):
        if self.__only_you == False:
            self.name = name   # 初始化名字
            self.__only_you = True  #成为了唯一
    def __new__(cls, *args):
        if cls.__girl == None:
            cls.__girl = object.__new__(cls)  #创建第一个女朋友 实例
        return cls.__girl

girl01 = GirlFriend('白冰')
print(girl01.name)
girl02 = GirlFriend('美丽')
print(girl02.name)

