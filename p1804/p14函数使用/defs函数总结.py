
# 总结函数的使用
'''

#无参 函数
def 函数名称():
    行数执行语句
'''

def print_line():
    print("----------")

#print_line() # 无参函数的使用,调用

# def 函数名(型参):
def print_user(a): #一个参数
    print(a)

#print_user('*'*30)

# def 函数名(参数1, 参数2):
def add(a, b):
    #print('a+b') # 1.引号引起来的，会原样输出;
    #print (a)   # 2.直接写变量，会打印变量保存的数值;
    #print (a+b)   # 3.如果是变量运算，直接打印运算结果;
    return a+b

s = add(1,2)
print (s)



def question(s):
    print(s)
    xinli = "我才不饿呢。"
    return xinli

r = question("你饿吗？")
print (r)













