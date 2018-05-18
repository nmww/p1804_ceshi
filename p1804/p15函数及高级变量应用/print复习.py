
# 复习  print  打印输出的使用

print ('字符串，会被原样输出;')
print ("hello world!")
print (123)
print ('你好' + '中国')
print (5 + 6)
print ('5' + '6')
print ('i miss u' * 3)
#------------------------

name = '张三'
age = 22
print (name)
print ('您要打印的姓名是：'+name)
print ('您要打印的姓名是：%s' % name)

print ('您的姓名是：%s，您的年龄是：%d' % (name, age))
print ('您的姓名是：%s,\n您的年龄是：%d' % (name, age))
print ('您的姓名是：%s,\t您的年龄是：%d' % (name, age))

print ('您的姓名是：%s,\t您的年龄是：%d' % (name, age), end='岁.')

#-----------------------
tup = (1,'a',2)
print (tup[0])
print ('元祖的第一个数据是：',tup[0])
print ('元祖的第一个数据是：%d' % tup[0])



