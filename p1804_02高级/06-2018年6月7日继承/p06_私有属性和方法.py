#-*-coding:utf-8-*-

class People:
    def __init__(self, name, salary):
        self.__name = name   # 声明了 这个属性 为 类私有
        self.salary = salary
    def get_name(self):
        return self.__name
    def set_name(self, n):
        self.__name = n
        return self.__name
    def get_salary(self):
        return self.salary

    def __send_msg(self):
        print ('验证码发送成功')

    def get_msg(self):
        '''这个方法给用户提供，获取验证码'''
        return self.__send_msg()

xiaohua = People('小花',6000)
print( xiaohua.get_name()  )
xiaohua.set_name('小白')
print( xiaohua.get_name()  )
xiaohua.get_msg()

laowang = People('老王', 2000)