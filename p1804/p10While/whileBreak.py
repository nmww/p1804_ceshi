
# 重点 介绍 break 的使用
'''
while循环中，在循环未结束之前，希望跳出循环，
请使用 break
2.
3.
'''

a = 1

while a < 100:
    print ("%d"% a)
    if a == 50:
        print ("a=50了，循环从这里要终端，系统调用了break")
        break
    a = a+1

