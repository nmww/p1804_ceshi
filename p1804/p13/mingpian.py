

def systemMenu():
    ''' 名片管理系统，功能菜单展示'''
    print ('*'*30)
    print ("欢迎使用【名片管理系统】V1.0")
    print ("1. new")
    print ("2. search all")
    print ("3. search one")
    print ("4. delet card")
    print ("5. exit")
    print ('*'*30)

def tuichu():
    print ("成功退出名片管理系统")

def newCard():
    pass

def sAll():
    pass

def sOne():
    pass

def delCard():
    pass


systemMenu()

while True:
    user = int(input("请数如你希望的操作对应的编号："))
    if user == 1:  # 创建名片
        newCard()
    elif user== 2: # 查看全部
        sAll()
    elif user== 3:  # 查看一个名片
        sOne()
    elif user== 4:  # 删除一个名片
        delCard()
    else:   # 退出
        tuichu()
        break


