#coding=utf-8
#结果 = ax + b
#y = 2x + 3

def wai(a,b):
    def nei(x):
        nonlocal a #在声明之前，一定不能被使用,包括打印
        print ('y=%d*%d+%d' % (a,x,b))
        a += 1
        y = a*x+b
        return y
    return nei

w = wai(2,3)
print (w(3))

