
dic = {'name':'张三',
        'age':18,
        'sex':'nan',
        'phone':110}
dic2 = {'name':'张三11111111111',
        'age':18,
        'sex':'nan',
        'phone':110}



dic['name'] = '李四'
#dic['email'] = '123@qq.com'

#print (dic)
#print (dic['name']) #通过 key 查找打印，对应的 数据

com = input('请输入公司:')
dic['com'] = com
#print (dic)

list_mingpian = [] #list
list_mingpian.append(dic)
list_mingpian.append(dic2)
print (list_mingpian)



