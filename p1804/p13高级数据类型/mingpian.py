

import card_tools

list_card = [] # 空列表，用于保存名片dic
'''
dic
company : 北财科技
name : 张三
手机号： 110
'''

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

'''
def newCard():
    print('*'*50)
    print("开始创建名片")
    name = input("请输入姓名：")
    com = input ("请输入公司名:")
    phone_num = input("请输入手机号:")
    dic = {'name':name,'company':com,'phone':phone_num}
    list_card.append(dic)
    print(list_card)
    print("名片保存成功，姓名是：%s" % dic['name'])
    pass
'''

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
        card_tools.newCard()
    elif user== 2: # 查看全部
        sAll()
    elif user== 3:  # 查看一个名片
        sOne()
    elif user== 4:  # 删除一个名片
        delCard()
    else:   # 退出
        tuichu()
        break


