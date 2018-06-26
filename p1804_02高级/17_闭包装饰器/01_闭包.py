#coding=utf-8

def wai(start=0):

    def nei():
        #说明要访问的变量是外部函数的
        nonlocal start
        start += 1
        print(start)
        #return '自定义'

    return nei

a = wai(1)
print(a())
a()
a()
b = wai(1)
b()



