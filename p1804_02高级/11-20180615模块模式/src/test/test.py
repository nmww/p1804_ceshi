
import sys
p = '/home/cc/git_workspace/p1804_02高级/11-20180615模块模式/src'
sys.path.append(p)
print(sys.path)
#sys.path.append('..')
#/home/cc/git_workspace/p1804_02高级/11-20180615模块模式/src
# src/test
# src/mtest
from mtest.t01 import *
from mtest.t02 import *
a()
b()
