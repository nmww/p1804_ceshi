
#文件打开与关闭操作

#如果文件已经存在，直接打开
#如果文件不存在，系统会 先新建文件hello.doc，然后打开
fname = open('hello','w') # open打开文件名是hello.doc的文件;
#当文件不存在的时候，会报错，只针对已经存在的文件，进行打开读取
f = open('hello.doc','r')
f = open('hello1.doc','a')
f = open("new.txt",'wb+')

#关闭已经打开的对应文件
fname.close()
f.close()
