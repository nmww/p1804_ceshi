
# while 循环条件：
a = 8  # 初始/起始 数值
while a != 8:  # 循环条件
    a = a+3  #  每次循环 步长
    print ("hello world")
#控制循环次数的三个关键点
#1. 初始数值
#2. 循环条件
#3. 步长

a = 1
while a <= 10:
    #print ("%d "% a)
    # n%2 == 0  偶数  不是偶数就是 奇数
    if a%2 == 0:
        print("%d 是偶数" % a)
    else:
        print("%d 是奇数" % a)
    a = a+1


