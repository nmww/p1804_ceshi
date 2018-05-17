# 演示 函数 之间的调用，使用

# 定义一个 函数 ：  打印输出 一行 ×

'''
def p_line():
    print("*"*30)
'''
# 知识点1. 函数之间的 调用
# 知识点2. 函数文件的引用 import
# pdef.py  p_line()
# 使用其他文件中的函数
# 1. import 文件名
# 2. 文件名.函数名（）

# p_line() #函数的调用，使用
import pdef

a = 0
while a<3:
    #p_line()  # 对函数进行调用，或使用
    pdef.p_two()
    a += 1




