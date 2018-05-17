'''
if
while

if
    if
while
    while
'''
# 男 60岁退休 继续奋斗 娶媳妇
# 女 55岁退休 继续努力 生孩子

sex = input("请输入性别：")  # 获取键盘输入的性别
age = int(input("请输入年龄：")) # 获取输入的年龄，转换类型为整数

if sex == '男':
    if age <= 60:
        print ("继续奋斗，多取媳妇。")
    else:
        print (">60 岁允许退休，安详晚年.")
else:
    if age <= 55:
        print ("继续努力，多生孩子，多种树。")
    else:
        print (">55 岁，允许加入广场无大妈群。")








