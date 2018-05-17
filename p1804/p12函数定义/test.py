

def jia(a,b):
    s = a + b
    print (s)
    return a+b

def printInfo(name, age):
    print ('your name = %s'% name)
    print ('your age = %s'% age)

n = "zhangsan"
a = '180'

printInfo(n,a)
printInfo(n,'20')
printInfo('baibing',a)
printInfo('lisi','22')

# None
s = jia(1,2)
print (s * 8)




'''
1. 完成计算器的基本运算
2. 增加友好提示，欢迎使用计算器
3. 让计算器循环的获取用户的输入，给出计算结果
4. 退出计算条件判断， 当用户输入 q退出 计算器循环
5. 增加 用户输入内容的 非法验证，给出正确提示
思考：
6. 2个以上的 多个数的计算 如何实现
'''


