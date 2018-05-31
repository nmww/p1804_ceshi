

list1 = []  # 保存字典 名片
dic1 = {'name':'zhangsan','com':'北财科技', 'qq':123}    # 每一个名片 是一个字典
dic2 = {'name':'lisi','com':'清华紫光', 'qq':121233}
dic3 = {'name':'wangwu','com':'百度科技', 'qq':220}
dic4 = {'name':'寒冰','com':'联想集团', 'qq':110}
dic5 = {'name':'张婷','com':'同仁堂', 'qq':120}
dic6 = {'name':'崔健','com':'物美超市', 'qq':119}

list1.append(dic1)
list1.append(dic2)
list1.append(dic3)
list1.append(dic4)
list1.append(dic5)
list1.append(dic6)

#print (list1)

na = input("请输入要查询的名字：")
for i in list1:
    if na == i['name']:
        print ('*'*30)
        print ('姓名：%s' % i['name'])
        print ('公司：%s' % i['com'])
        print ('QQ号：%s' % i['qq'])





