#-*-coding:utf-8-*-

try:
    print('name')

    try:
        for i in range(1.10):
            print(i)
    except TypeError:
        print('for 循环 出问题了')

except IOError as a:
    print(a)

