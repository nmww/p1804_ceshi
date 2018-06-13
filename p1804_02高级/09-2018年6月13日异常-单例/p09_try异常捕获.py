#-*-coding:utf-8-*-
'''
1. 什么是异常   error
2. 单个异常  try :    except a:
3. 多个异常  try:     except (a,b,c):
4. 异常显示  as a :
5. 全部异常  try:    except Exception as a:
6. 异常捕获最终要执行的 方法 ：  finally
'''

try:  #希望 抓获 哪一部分代码，可能出现的异常
    print(1)
    phone_number = input('请输入手机号码：')
    print( int(phone_number) )
    # open('a.txt','r')
    # print(name)
    # print('%d'% 'name')
    print('zhangsan')
    print(True)
except Exception as error_result:  # 当出现了指定异常，我们希望执行的操作
    print('程序出现了问题 : %s' %  error_result)
else:
    print('程序没有任何问题')