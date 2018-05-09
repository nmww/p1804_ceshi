price = 3.5
weight = 3

# print ("西瓜价格是 %d 元，重量是 %d 公斤" % (price, weight))
# print ("西瓜价格是 %06d 元，重量是 %03d 公斤" % (price, weight))
# print ("西瓜价格是 %.2f 元，重量是 %d 公斤" % (price, weight))
# print ("西瓜价格是 %.2f 元，重量是 %d 公斤 %%" % (price, weight))

'''

print 
%d  --- >  整数
%06d --->  6位的整数  ： 1 ->   000001
%02d --->  2位的整数 ：  2 -> 02
%03d --->  3位的整数 ： 12 -> 012

%f  --->  浮点类型数据  有小数点的数据 3.1415926
%.3f --->  小数点后保留 3 位   3.141
%.1f --->  小数点后保留 1 位   3.1

%s   ---> 字符串
	'  '   "  "
%%   ---->   %
'''

age = 20
print ("您的年龄是 %d 岁" % (age) )
print ("您的年龄是 %05d 岁" % (age) )

price = 13.14000000000000
print ("你的身价是 %f 美元" % (price))
print ("你的身价是 %.7f 美元" % (price))
print ("你的身价是 %.2f 美元" % (price))

email = '2423@qq.com'
print ("您的邮箱是 %s ;" % (email))

jigelv = 90
print ("班级周考及格比例是: %d %% " % (jigelv))


print ("您的邮箱是 %s; \n  您的身价是 %.2f; \n 您的年龄是 %d;"
% (email, price, age))



