# -*-coding=utf-8-*-
# yield generator

# 1-100  奇数
# while  for   list []
l = [i for i in range(1,101) if i%2 != 0]
print (type(l))
print (l)

l = (i for i in range(1,101) if i%2 != 0)
print (type(l))
print (l)

def a():
    for i in range(1,101):
        if i%2 != 0:
            yield(i)

l = a()

