
#1. 全局变量:函数内容和外部都可以访问
#2. 局部变量:只能在本函数内容进行使用或者访问


list_card = ['zhangsan',22,'nv']  # 全局变量 列表
# 列表 修改内部数据，不需要用 global 声明
a = 100 # 全局变量 函数作用域之外
def test1():
    global a # 全局变量 使用修改 关键字
    a += 1
    print (a)
    c = 1 # 函数作用域里边的 遍历为局部变量
    list_card[2] = 'nan'
    list_card.append('001')
    print (list_card)

def test2():
    print (a)
    #print (c) #无法访问，其他函数的局部变量

#print (c)  #外部 无法访问，函数内容的局部变量

test2()
test1()

