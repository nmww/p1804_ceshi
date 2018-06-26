#coding=utf-8
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
@makeBold
def test1():
    return "hello world-1"
@makeItalic
def test2():
    return "hello world-2"
@makeBold
@makeItalic
def test3():
    return "hello world-3"

t1 = test1()
t2 = test2()
print (t1)
print (t2)
print (test3())



