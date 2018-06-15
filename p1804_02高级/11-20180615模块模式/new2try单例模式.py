# 单例模式

class MyError(Exception):
    def __init__(self,name):
        self.name = name

try: #抓异常
    pwd = input('请输入用户密码：')
    try:
        if len(pwd) < 6:
            raise MyError('你的密码太短了，最少要6位：%s' %  pwd)
    except (NameError,IOError) as e:
        print('===== %s ' % e)
    finally:
        print ('file is closed')
except Exception as s:
    print (' 外层 ：error: %s' % s)
else:
    print('else 程序没有任何问题，会执行这里')
finally:
    print ("finally try执行完成，不论是否有异常，都要执行这里")






