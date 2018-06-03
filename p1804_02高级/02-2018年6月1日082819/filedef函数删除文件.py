

# def 方法/函数名称(型参):  *变量名=tup  **变量名=dic
#   相同缩进的是函数内 语句


import os
def shanchu(file_name):
    ''' 该函数用于删除给定的文件名对应的文件 '''
    os.remove(file_name)

shanchu('1.txt')





