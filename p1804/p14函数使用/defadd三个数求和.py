

#1. 写一个函数
#2. 求三个数的和
#3. 求三个数的平均数

def add(a,b,c):
    return a+b+c

def pingjun(x,y,z):
    s = add(x,y,z)
    return s/3

s = add(1,2,3)
print(s)

p = pingjun(10,10,10)
p = pingjun(1,10,20)
print(p)
