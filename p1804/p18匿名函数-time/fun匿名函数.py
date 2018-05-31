
# 匿名函数
# lambda

def add(b,a=1):
    return a+b

print( add(2) )

# 1. 简单使用
a = lambda a,b : a+b
b = lambda x,y : x-y
c = lambda a,b,c : a+b+c
print (c(1,2,3))
print (a(1,2))
print (b(2,1))
# 2. 默认值使用
d = lambda x,y=1,z=2 : x+y+z
f = lambda a : a**2
print ('------',d(1))
print ('------',f(4))
# 3. 列表中使用
l = [(lambda a:a**2),(lambda b:b**3),(lambda c:c**4)]
ll = [(lambda a,c:a+c),(lambda a,c,d:a+c+d)]
print ('----------',l[0](3))  # 3**2  == 3*3 = 9
print ('----------',l[1](4))  #  4**3 == 4*4*4  =64
print ('----------',l[2](2))  #  2**4 == 2*2*2*2 = 16
# 4. 字典中的匿名函数 无参匿名函数
d = {'f1':lambda:2+3, 'f2':lambda:2*3}
print ('得到字典f1的匿名函数，调用：',d['f1']())
print ('得到字典f2的匿名函数，调用：',d['f2']())





