
print ("你好")
# 有关高级变量知识的补充 和完善
# list   tup   dic   strint应用

list_name = ['a','b','a','c']  # l = []
len(list_name)  #求列表的长度，或者是列表有几个元素
list_name.count('a')  # 'a'在列表中出现了几次

list_name[0]  # 取得列表 下标 是0位置的 数据  即 ‘a'
list_name.index('b')  # 查询 指定元素/数据'b' 在列表中的位置/下标

list_name.append('b')  # 在列表最后边 追加一个 指定的元素 'b'
list_name.insert(0,'d')  # 在指定位置0，插入给定的元素 'd'
list_name.extend(list_name)  # 将指定的列表 链接  到 原来的列表后边

list_name.pop()   # 弹出list最后一个元素/数据
list_name.pop(1)  # 弹出 指定 下标对应的 数据
list_name.remove('a')  # 将 指定的数据  从list中 移出
del list_name[0]  # 删除 指定下标 对应的数据

list_name.sort()  # 升序排列
list_name.sort(reverse=True)  # 降序排列
list_name.reverse()   # 反转   465  == > 564
#---------------
# 元组   dic

#list = [{ k:{}, k:{} }]
dic  = {'name':'张三', 'age':22, 'sex':'男', 'height':'110',"weight":50}
dic['name']  # 通过指定的 key 'name'， 获得 对应的 values '张三' ， 如果name不存在，系统报错
dic.get('name')  # 同上   唯一区别是：  name不存在的时候，不会报错

#print (dic.get('name'))
#print (dic['phone'])  #  KeyError: 'phone'
#print (dic.get('phone'))  # None   当指定 key不存在时候，get 返回  None 不存在


# k_list = dic.keys()   # 快速获得 字典中的 所有key， 返回一个 list
# print (dic.keys())  #dict_keys(['name', 'age', 'sex'])
# print (k_list)
# v_list = dic.values()  # 获得所有  values数值   返回一个 list
# print (dic.values())
# print (v_list)
# kv_list = dic.items()   # 获得 所有  k:v   返回一个 list
# print (dic.items())
# print (kv_list)
#  创建一个 字典， 里边有  5条数据；  key 和 values 自定定义
#  分别输出  字典的 全部 key
#  分别输出 字典的 全部 values
#  循环 输出  每一组  字典的 元素

tup  = ('name','zhangsan')

# print (type(dic.items()))
# for k,v in dic.items():
#     print("k = ",k)
#     print('v = ', v)

'''
北京 面积 100平米
北京 人口 200W
上海 面积 60平米
上海 人口 150W
'''
#list = [{'北京':{'面积':'100平米' , '人口':'200W'} , '上海':{'面积':'60平米' , '人口':'150W'}}]
list = [{'北京':{'面积':'100平米' , '人口':'200W'} , '上海':{'面积':'60平米' , '人口':'150W'}
         , '成都':{'面积':'160平米' , '人口':'50W'}}]
# key 一定要用 字符串；  values 可以是任意类型
# for i in list:
#     for a,b in i.items():
#         for c,d in b.items():
#             print (a, c, d)

dic  = {'name':'张三', 'age':22, 'sex':'男',"weight":50, 'height':'110'}
# dic.pop('name')
#dic.popitem()   # 弹出 最后一组 item  k:v
#del dic['name']
#dic.clear()

d = {'北京':{'面积':'100平米' , '人口':'200W'}}
# dic['name1']  =  'lisi'         #修改  添加
dic.setdefault('sex','男')   # 不存在添加，存在无操作
dic.update(d)   #  将新字典 更新 到 原来字典的 后边
print( dic)  #  list  extend





















