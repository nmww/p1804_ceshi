#-*-coding:utf-8-*-

file_name = input('请输入想要打开的文件名称：')
f = open(file_name, 'r')
try:
    print(a)
    content = f.read()
    print(content)
except Exception as r:
    print(r)
finally:
    f.close()

print(f.closed)
print('-----------------')

