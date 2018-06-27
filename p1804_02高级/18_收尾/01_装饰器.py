#coding=utf-8

# == 装饰器
#1. 无参数
def wai(fun):
    def nei():
        print ('==函数调用前的检查==')
        fun()
    return nei
@wai
def foo():
    print('==foo==')
#foo()

#2. 有参数
def wai(fun):
    def nei(*args): #闭包
        print ('检查 传递的参数是   ' , args)
        print ('==函数调用前的检查==')
        fun(*args)  # 函数调用，传递实际参数   foo(1)
    return nei
@wai
def foo(*args): #函数定义
    print('==foo==')
    print('==foo== 参数是  ' , args)
#foo(1,2,3,4,5)

#def a(*args):
#    print (args)
#a(1,2,3,4)

#3. 不定长参数
def wai(fun):
    def nei(*args, **kwargs):
        print ('检查传递的参数是' , args)
        print ('==函数调用前的检查==')
        fun(*args, **kwargs)
    return nei
@wai
def foo(*args, **kwargs): # *a ()  **a {}
    print('==foo==')
    print('==foo== 参数是' , args)
    print('==foo== 参数是' , kwargs)

#foo(1,2,3,4,3,4,5,6,'a',a=1,b=2,c='a')

#4. 返回值
def wai(fun):
    def nei():
        print ('==函数调用前的检查==')
        return (fun()) #2
    return nei
@wai
def foo(): #1
    return ('==foo==')

#print (foo()) #3

#5. 增加外部 参数传递
def jsq(a): # 1.最外层添加 方法
    def wai(fun):  #传递的函数的引用
        def nei():  #传递的 函数所需要的 参数
            print ('==函数调用前的检查==')
            print ('判断需要使用参数 这里 接受 ', a)
            return (fun()) #2
        return nei
    return wai  #2. 返回 最近的内层函数
@jsq(12345)  # 3. 调用最外层的装饰器 名称 (传递参数)
def foo(): #1
    return ('==foo==')

foo()










