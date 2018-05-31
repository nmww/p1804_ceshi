
# for 循环的复习总结
# 遍历  str  整数  tup list  字典
# 1.str
name = 'zhangsan'
name1 = '李四'
for i in "zhangsan":
    print (i)
for i in name:
    print (i, end = '\t')

print ('\n')

a = 0
for i in 'zhangsan':
    a += 1
    print ('第 %d 个字母是什么：%s' % (a , i))

#--------------------------------
print ("元组输出".center(20,'*'))
tu1 = (1,2,3,4,5)
for i in tu1:
    print (i)
for i in range(0, len(tu1)):
    print (tu1[i])
li = [1,2,3,4,5]

#-------------------------------
# 复合类型的数据
print ("复合数据类型输出".center(20,'*'))
li1 = []
tup2 = (1,2,3)
tup3 = (1,2,3)
tup4 = (1,2,3)
li1.append(tup2)
li1.append(tup3)
li1.append(tup4)
# [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
print (li1)
for i in li1:
    #i == 一个元组
    for j in i:
        print (j)
print ("复合数据类型  用下标遍历".center(20,'*'))

for i in range(0, len(li1)):
    tu = li1[i]
    for j in range(0, len(tu)):
        print (tu[j])












