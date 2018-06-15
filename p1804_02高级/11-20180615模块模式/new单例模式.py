# 单例模式

class Father(object):
    def a(self):
        print ('a')
    def b(self):
        return 1112

class Son(Father):
    xinqing = True # 表示心情开
    def a(self):
        print('a')
    def b(self):
        if Son.xinqing == True:
            return Father.b(self)
        return 1

s = Son()
s.a()
print(s.b())


