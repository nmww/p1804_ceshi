
def b(fun): # 接收希望处理的 函数
    def c(): # 处理逻辑
        print('1')
        print('2')
        print('3')
        fun() # 调用希望执行的原函数
    return c # 封装好的闭包返回

@b
def a(): # 函数本身
    print('==a==')

a()

