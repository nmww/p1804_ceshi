
# 元组 数据类型
# 关键字  Tuple
# 特点： 内容不可更改

t = () # 定义了一个 空 元祖
t1 = ('zhangsan', 22, '男') #定义了一个有数据的元组
t2 = ('张三',)  # 定义了 有一个数据的元组 结尾要用‘，’
print (t2)
print (type(t2))

print (t1[2])  # 根据下标 2 找到 对应的元组数据
print (t1.index(22)) # 用 index  查找 22在元组中的小标
# 元组的格式化输出
print ('姓名是 %s \n年龄是 %d \n性别是%s \n'% t1)

# 元组遍历
for i in t1:
    print (i)

