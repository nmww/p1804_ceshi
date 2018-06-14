#-*-coding:utf-8-*-

# 通过开关 控制 是否 抓取异常信息
class Test(object):
    def __init__(self):
        self.switch = 'open'    #初始化开关 实例属性
    def div(self, a, b):
        try:
            return  a/b
        except Exception as ret:
            if self.switch == 'open':
                # 对异常进行处理
                print('出现了异常： %s' %  ret)
            else:
                raise # 不处理异常，直接抛出到上一层

t = Test()
t.switch = 'close'
print(t.div(2,0))


