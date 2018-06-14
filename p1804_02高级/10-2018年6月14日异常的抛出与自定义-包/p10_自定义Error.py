#-*-coding:utf-8-*-
# 自己定义一个异常
# NameError IOError TypeError SyntaxError
class MyError(Exception):  #自定义 需要的异常提示
    def __init__(self, name, age,sex):
        self.name = name
        self.age = age

# raise  抛出 异常
def get_pwd():
    pwd = input('请您输入密码：')
    if len(pwd) < 6:
        raise MyError('密码小于6位不符合要求！！！！', 12, '女')

try:
    get_pwd()
except Exception as re:
    print('遇到了异常：内容是 %s' %  re.age)

