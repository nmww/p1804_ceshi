

list_card = [] # 空列表，用于保存名片dic
def newCard():
    '''新建名片'''
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


