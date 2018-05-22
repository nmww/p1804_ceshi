
# 递归函数
# 函数调用自己的过程 就是递归

# 函数 -> 方法 使用def

def a():
    print ("a 函数")

def b():
    print ("b 函数")


# 阶乘  比如 3！ ==  1×2×3
def jiecheng(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

#s = jiecheng(3)
#print ('阶乘结果是：%d' % s)
# n! = n*(n-1)!
# (n-1)!  == digui(n-1)
# 1. 递归的 结束条件
# 2. 递归的 模式 n*(n-1)!
def digui(n):
    #n*(n-1)!
    s = 0
    if n>=1:
        s = n*digui(n-1)
    else:
        s = 1
    return s

def dijia(n):
    s = 0
    if n>=1:
        s=n+(n-1)
    else:
        s=1
    return s

#n = digui(5)
#n = dijia(10)
print ('result == %d' % n)




