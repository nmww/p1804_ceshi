#coding=utf-8

# generator 生成器 yield()
def a():
    n = 0
    while n<100:
        #print n
        yield(n)
        n += 1
gen = a() #生成器
next(gen) # StopIteration

# Iterator  迭代器 iter()
l = []
d = {}
t = ()
it = iter(l) #迭代器
next(it)  # StopIteration

# Iterable  可迭代 isinstance(obj  , Iterator/Iterable )
isinstance(it, Iterable)
isinstance(it, Iterator)
isinstance(gen, Iterator)
isinstance(gen, Iterable)



