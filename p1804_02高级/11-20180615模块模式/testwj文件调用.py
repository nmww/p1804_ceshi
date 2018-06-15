# 如何导入不同文件夹种的 模块

# 1. 在需要的文件夹中，建立空的文件  __init__.py
# 2. import 文件夹名.文件名
# 3. 使用： 文件夹名.文件名.方法名()

#import mod.mod1
#mod.mod1.mod1()

#4. from 文件夹名.文件名 import *
#5. 使用 直接使用 方法名称
import sys # 这里导入了一个sys系统模块
print (sys.path)

from mod.mod1 import *
mod1()
