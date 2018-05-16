
list_name = [] # 空列表创建

while True: #循环
    # 获得用户输入的姓名
    name = input("请您输入要加入到列表的姓名：")
    list_name.append(name) #姓名保存到列表
    if name == 'q': # 输入q 退出循环
        break
print (list_name) #输出全部列表
# 打印 3/5/8/10 位置的姓名
print ('第 3 位是：%s' % list_name[3])
print ('第 5 位是：%s' % list_name[5])
print ('第 8 位是：%s' % list_name[8])
print ('第 10 位是：%s' % list_name[10])
# 对列表进行 排序 并 打印
list_name.sort()
print (list_name)
# 倒序  打印
list_name.sort(reverse=True)
print (list_name)
# 弹出 最后一个 同学 打印
print (list_name.pop())
# 删除第 8 人  打印
del list_name[8]
print (list_name)
# 创建 第二个 列表 n
n = [1,2,3,4,5,6,7]
# n 列表追加到  list后
print (list_name.extend(n))
# 查询 小明  所在的下标
print (list_name)
print ('小明所在位置：%d '% list_name.index('小明'))


