#coding=utf-8
# 斐波那契数列
# 1,1,2,3,5,8 ;;;

def fib(day):
    n = 0
    a,b = 0,1
    while n < day:
        yield(b)
        a,b = b,a+b
        n += 1 # 天数递增
    #python 3 使用yield可以继续 return
    #python 2 使用yield需要注销 return
    #return 'ok'
a = fib (100)
print (next(a))
print (next(a))
print (next(a))

