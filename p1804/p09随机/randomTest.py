'''
random 随机函数
1. 原文件开头  import random
    导入 random  函数包
2. 使用的位置  random.randint(开始整数,结束整数)
    random.randint(1,100)  随机1-100的任意整数
'''

import random

a = random.randint(1,10)
print ('随机的a =  %d ' % a)
b = random.randint(10,10)
print ('随机的b =  %d ' % b)
# c = random.randint(20,10)  # 错误的使用方法
# print ('随机的c =  %d ' % c)


