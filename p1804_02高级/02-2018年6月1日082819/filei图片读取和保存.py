
# 打开图片并特殊保存

f = open('img61.jpg','rb+')
cimg = f.read()
print(cimg)
f.close()

f = open('2.txt','wb+')
f.write(cimg)
f.close()

