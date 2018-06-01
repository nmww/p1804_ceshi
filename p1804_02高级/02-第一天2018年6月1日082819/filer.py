
# 对一个文件进行 读写
f = open('1.txt','w')
f.write('白日依山尽,\n')
f.write('黄河入海流.\n')
f.close()

f = open('1.txt','r')
#c = f.read()  #  read()  读取全部文件内容
#c = f.read(2)  # read(num)  读取 给定数字个数的 内容
#c = f.readlines()  # 读取所有的 行内容
c = f.readline()  #读取一行

'''
for i in c:
    print (i)
    print (type(i))
'''

print (c)
print (type(c))
f.close()

f = open('1.txt','a')
f.write('-*-')
f.close()
f = open('1.txt','r')
c = f.read()
print(c)
f.close()

f=open('1.txt','a')
f.write(c)
f.close()



