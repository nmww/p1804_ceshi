f = open('1.txt','w')
f.write('鹅鹅鹅，曲向向韩笑\n')
f.write('白毛浮绿水，韩笑一片绿\n')
f.close()

'''
f1.read(2)
f1.read(2)
c = f1.read(3)
b = f1.read(30)
print ('b的内容是 %s'% b)
'''

f1 = open('1.txt','r')
c = f1.readlines()

f2 = open('1.txt','w+')
for i in c:
    #'abcd\n'
    s = i[:len(i)-1]
    f2.write(s+"*\n")

f1.close()
f2.close()

print ('文件的名字是 %s' % f2.name)
print ('文件是否已经关闭 %s '% f2.closed)
print ('该文件的打开模式是 %s ' % f2.mode)




