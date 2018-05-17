
# 加法运算
# 默认参数 y = 2
def addSum(x,y=2):
    print ('x= %d '% x)
    print ('y= %d '% y)
    sum = x + y
    print (sum )
addSum(x=1)

# 两个型参
def addSum(x,y):
    sum = x + y
    print (sum )
addSum(1,2) # 顺序传递 赋值引用
addSum(y=2,x=5) # 按照赋值传递，不考虑顺序
addSum(2,y=1) # 单独制定 赋值 只能在最后位置
