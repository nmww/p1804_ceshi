#-*-coding:utf-8-*-

# 人
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def set_salary(self, new_salary):
        if new_salary > self.salary:
            self.salary = new_salary
        else:
            print('我拒绝')

    def get_salary(self, shenfen):
        if shenfen == '媳妇':
            return  1000
        elif shenfen == '朋友':
            return 1000000
        elif shenfen == '老爹':
            return self.salary
        else:
            return 0

gtq = Worker("光头强",10000)
gtq.set_salary(12000)
print( '====工资现在是 = %d' %   gtq.salary)
# while True:
#     shenf = input("想知道我的工资吗，请说明你的身份：")
#     if shenf == 'q':
#         print ('无可奉告')
#         break
#     print('光头强的工资是 %d ' %  gtq.get_salary(shenf))





