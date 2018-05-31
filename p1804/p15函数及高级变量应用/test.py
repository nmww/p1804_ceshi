

# 型参  比喻成 盒子
# 变量  比喻成 盒子

def add(a,b):
    print (a)
    print (b)
def add(*anything):
    print (anything)
def addsan(a,b,c):
    a+b+c

re = 0
def add_some(*num):
    global re
    for i in num :
        re = i+re
    print (re)

add_some(1,2,3,4,5,6)
add_some(1,20,300,4,5,6)

#tup = (1,2,3,4,5,6)

# 1- 10
#a = 0
#for i in tup:
#    a = a+i

#print (a)

a = 1
a = 'a'
a = [1]
a = {}
a = ()


