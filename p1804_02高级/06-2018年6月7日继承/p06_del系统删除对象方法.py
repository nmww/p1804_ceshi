#-*-coding:utf-8-*-

# __init__   系统默认方法； 用于类的初始化信息； 类创建的时候被调用
# __str__   系统默认方法： 用于返回print 打印类对象 时显示的内容；  当打印对象时候被调用；
# __del__   系统默认方法： 当创建的对象被删除/销毁的时候 系统自动调用；
'''
两种情况 __del__  会被系统 自动调用执行
1. 当类程序执行结束，系统自动销毁  没有引用的对象（不再使用的对象）
2. 当对象 被彻底删除/销毁的时候，系统会自动调用 del方法；   引用
'''
class Animal:
    import os
    def __init__(self, name, f):
        self.name = name
        self.f  =  f# = open('name.txt',what)
    def get_name(self):
        self.name = self.f.read()  #读取文件
        return  self.name
    def __del__(self):
        self.f.write(self.name)  #写入文件
        self.f.close()
        print ('-----当前的对象被销毁了-----')

dog = Animal('', open('name.txt', 'r'))
print(dog.get_name())

dog.f = open('name.txt', 'w')
dog.f.write('旺财')

print ('==============================')
'''
练习题： 
1. 退出时候，保存名字
2. get的时候 得到文件里的名字
结合以上代码：增加get_name和set_name方法；
当调用set_name 方法时候，优先判断 本地 name.txt文件是否保存了名字，如果保存则读取并返回，否则返回默认名字；
当程序退出时候，将当前对象的姓名，通过get_name方法，保存到本地文件 name.txt中；
1. def 定义两个方法
2. 判断： 打开open 文件  读取文件内容read  判断内容if
3.  get_name:    open   write ( self.name )     ;     
'''
