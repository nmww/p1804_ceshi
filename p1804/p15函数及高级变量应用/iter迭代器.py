#!/usr/bin/python3

import sys #引入 sys包
# iter 生成迭代器进行循环

list1 = [1,2,3,4]
it = iter(list1)
while True:
    try:
        print (next(it))
    except StopIteration:
        print (StopIteration)
        sys.exit()


