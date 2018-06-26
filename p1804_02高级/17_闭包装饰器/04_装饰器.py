#coding=utf-8
def f1():
    print ('==f1==')

def f2():
    print ('==f2==')

def wai(fun):
    def nei(name):
##################################
        if name == '员工':
            fun()
        else:
            print ('此功能只提供给内部员工使用。')
##################################
    return nei

#wai()('员工')
a = wai(f2)
a('员工')


