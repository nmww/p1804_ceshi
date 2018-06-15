# 单例模式

class Father(object):
    flag = 'one'
    flag_name = 1
    def __init__(self, name):
        if self.flag_name == 1:
            self.name = name
            print ('init')
            self.flag_name = 2
    def __new__(self, *b):
        if self.flag == 'one':
            self.flag = object.__new__(self)
            return self.flag
        return self.flag

try: #抓异常
    f = Father('张三')
    print (f.name)
    f1 = Father('李四')
    print (f1.name)

    print(id(f))
    print(id(f1))
except Exception as s:
    print ('error: %s' % s)
else:
    print('else 程序没有任何问题，会执行这里')
finally:
    print ("finally try执行完成，不论是否有异常，都要执行这里")






