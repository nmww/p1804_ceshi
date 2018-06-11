#-*-coding:utf-8-*-
# 驴 + 马 = 骡子   （多继承）

class Donkey(object):
    '''驴类'''
    def manzou(self):
        print('走路慢……')
    def jiao(self):
        print ('驴在欢叫…*&%&￥……￥&（&*））*…')

class Horse(object):
    '''马类'''
    def naili(self):
        print('马力足，持久强……')
    def jiao(self):
        print ('马在嘶鸣………………')

class Mule(Donkey, Horse):
    '''骡子'''
    def jiao(self):
        print('Mule 在唱歌……')
    pass

骡子一号 = Mule()
骡子一号.manzou()
骡子一号.naili()
骡子一号.jiao()
print(Mule.__mro__)

