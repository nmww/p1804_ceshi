
def chuandic(c,*b,**a):
    print (c)
    print (b)
    print (a)

def chuandic1(**b):
    print (b)

#dics = {'name':'zhangsan', 'age':22, 'sex':'man'}
chuandic(1,2,3,2,4,name='zs',age=22,sex='woman')
chuandic1(a=1,b='hao',c='ok')


