#-*-coding:utf-8-*-

# 实例 属性  方法
# 类   属性  方法
# 静态方法  ：
class People(object):
    guoji = 'china'     # 类属性
    def __init__(self):
        self.name = '小明'    #实例属性
    def get_name(s):       #实例方法
        return s.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji
    @classmethod
    def set_guoji(cls):
        cls.guoji = '中国'
    @classmethod
    def say_chinese(c):
        print ('吧啦吧啦……中国话')
    @staticmethod
    def shegnqi():   # 静态方法
        print('生气了。')

# People.shegnqi()

class Tools(object):
    @staticmethod
    def menu():  # 静态方法
        print('*'*10)
        print('1. 上上签')
        print('2. 桃花签')
        print('3. 事业签')
        print('*' * 10)

    @staticmethod
    def print_s(s):
        Tools.menu()
        print(s," 1804班级 制作")

# Tools.menu()
# print('hello  world')
Tools.print_s('hello  china')
# People.guoji = 'usa'
# People.set_guoji()
# print(People.guoji)
# p = People()
# print(p.guoji)
