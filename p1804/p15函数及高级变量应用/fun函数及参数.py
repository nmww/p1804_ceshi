
def hanshu():
    print ('*'*30)
    print ("print 引号中的内容原样输出。")
    print ("这是一个无参函数。")

def hanshu1(canshu,c):
    print ('*'*30)
    print (canshu)
    print (a)

def hanshu2(*a): # 不定长参数
    ''' 函数想接收多个参数 ，可以使用
    def 函数名(*型参) '''
    print ("*"*30)
    print (a)

#hanshu()#调用 无参函数

a = 1  # 整数
c = 'zhangsan' # 字符串
b = [1,2,3,'b','c'] #  列表
canshu = {'k':'zhangsan','age':22} # 字典
#hanshu1(canshu, b) #调用有参函数
hanshu2(a,b,canshu)
