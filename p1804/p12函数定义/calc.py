
# 函数运算结果的 返回 用  return
def jia(a,b):  #加法
    #print (a+b)
    return a+b

def jian(a,b): #减法
    return (a-b)

def cheng(a,b): #乘法
    return (a*b)

def chu(a,b): #除法
    return (a/b)

'''
1. 基础 运算函数完成
2. 输入 内 = 容
3. 调用函数
'''

a = int(input ('输入第一个数字：'))
fuhao = input("请输入要做的运算符号：(+ - * /)")
b = int(input ('输入第二个数字：'))

if fuhao == "+":
    s = jia(a,b)
    print (s)




