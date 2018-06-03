
#定位seek
f = open('1.txt','w+')
f.write('举头望明月\n')
f.write('地上鞋两双\n')
f.close()

f = open('1.txt','r')
c = f.readline() # c 变量用于 保存 readline 返回的 一行内容
p = f.tell() # p变量用于 保存 tell返回的游标位置
print ('读取的第1行内容是： %s' % c)
print ('读取1行之后的游标位置是：%d' % p)

c = f.readline() # c 变量用于 保存 readline 返回的 一行内容
p = f.tell() # p变量用于 保存 tell返回的游标位置
print ('读取的第2行内容是： %s' % c)
print ('读取2行之后的游标位置是：%d' % p)

f.seek(0,0)
print (f.readline())

f.seek(-3,2)
print (f.tell())

f.close()





