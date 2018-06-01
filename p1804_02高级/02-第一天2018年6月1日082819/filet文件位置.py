
# tell  查看文件读写的 光标位置

# 偏移获取位置 计算的是 下标
f = open('1.txt','rb+')
#c = f.read(2)
f.seek(2,0)  # 从起始位置开始
position = f.tell()
print ('文件读取的开始位置 偏移 2 ： %d' % position)

f.seek(2,1)  # 从当前位置 读取 偏移数据
position = f.tell()
print ('文件读取的当前位置是偏移 2 ： %d' % position)

f.seek(-4,2)  # 从文件末尾开始
position = f.tell()
print ('文件读取的从结尾开始 偏移 -2： %d' % position)

f.close()
