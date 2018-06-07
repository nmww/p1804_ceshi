#-*-coding:utf-8-*-

class People:
    def __init__(self,name, yao, xiong, tun):
        self.name = name
        self.__yao = yao
        self.__xiong = xiong
        self.__tun = tun
    def ask_yao(self, sf):
        if sf == '医生':
            return self.__yao
        else:
            return 200
    def __sheng_wa(self):
        return '胖娃娃'

    def jie_hun(self, n):
        if n == '老王':
            print('太突然了，人家要考虑10000年！')
        else:
            print ('登记')
            print ('旅游')
            print(self.name + '给' + n + '生了一颗：'+self.__sheng_wa())

wyx = People('卫毅鑫',29,36,34)
s = wyx.ask_yao('医生')
# print(s)
wyx.jie_hun('郑程峰')
