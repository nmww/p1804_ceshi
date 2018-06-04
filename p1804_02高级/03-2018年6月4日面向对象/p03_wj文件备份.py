#-*-coding:utf-8-*-

# 1. 文件备份
# 2. 面相对象
# 文件备份
# 打开一个已存在的文件
# 将已经打开的文件 保存到新文件中
#cp 路径\源文件名 路径\目标文件名

def self_cp(oname):
    #1. 打开源文件； -----【old_file要备份的文件】-------
    old_file = open( oname ,'rb+')
    #old_file_name = old_file.name  #得到一件打开的文件名
    # 3.打开一个新的备份文件；
    p = oname.rfind('.')  # 找到文件中 .的位置下标
    name = oname[:p]  # 截取文件的名称部分
    namek = oname[p:]  # 截取文件的扩展名部分
    #-----【new_file  新保存用的文件 】-------
    new_file = open(name + '-副本' + namek, 'wb+')
    #2.读取源文件内容；
    # c = old_file.read()
    while True:
        c = old_file.read(1024)  # 读取 源文件
        if len(c) == 0:
            break
        # 4.将内容写入新文件里；
        new_file.write(c)       # 写入新文件 进行备份
    # 5.关闭打开的文件；
    old_file.close()
    new_file.close()

#0. 通过屏幕输入需要备份的文件名
n = input('请输入您需要备份的文件名称：')
self_cp(n)