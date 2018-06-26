#coding=utf-8
def wai(fun):
    def nei(name='员工'):
##################################
        if name == '员工':
            fun()
        else:
            print ('此功能只提供给内部员工使用。')
##################################
    return nei

#装饰器
@wai
def f1():
    print ('==f1==')
@wai
def f2():
    print ('==f2==')
f2()

#wai()('员工')
#a = wai(f2)
#a('员工')


