#coding=utf-8
def wai(fun):
    def nei(name='员工'):
##################################
        #if name == '员工':
        #    fun()
        #else:
        #    print ('此功能只提供给内部员工使用。')
        #    print ('你输入的名字是%s' % name)
        return '<nei=>'+fun()
##################################
    return nei

def wai1(fun):
    def nei1(pwd='123'):
##################################
        #if pwd == '123':
        #    fun()
        #else:
        #    print ('你的密码不正确。')
        #    print ('你输入的密码是%s' % pwd)
        return '<nei1=>'+fun()
##################################
    return nei1


#装饰器
'''
@wai
def f1():
    print ('==f1==')
'''
@wai1
@wai
def f2():
    return ('==f2==')

print(f2())

#wai()('员工')
#a = wai(f2)
#a('员工')


