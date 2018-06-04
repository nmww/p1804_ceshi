#-*-coding:utf-8-*-

'''
创建汽车类；
		用__init__ 初始化汽车属性；  lunzi = 4； color = ‘red’
	定义汽车的 通用方法：  跑、叫、追尾
	并创建多个汽车对象：宝马、福特、奥迪等
'''
class Car:
    def __init__(self, lz_num, color, name): # 类创建时，第一个执行的初始化方法
        self.lunzi = lz_num
        self.color = color
        self.name = name
    def run(self):
        print ("%s 跑起来了, %d 个轮子飞快转动起来 …… " % (self.name, self.lunzi))
    def jiao(self):
        print("%s 疯狂的吼叫中 …… "% self.name)
    def zhuiwei(self):
        print ("%s 选中了目标，准备追尾 …… "% self.name)
    def __str__(self):
        s = '车的名字是: '+self.name + " 车的颜色是： "+self.color
        return s

# print 打印类 对象，打印的内容是：  str方法返回的内容
bmw = Car(8,'green','宝马坦克')  # 对应的给 init初始化方法传递 参数 （构造方法）
print ('汽车的名称是 ： ', bmw )




# print( '宝马 的内存地址是 %d' % id(bmw) )
# fute = Car(4, 'red')
# print( ' 福特 的内存地址是 %d' % id(fute) )
# bmw.name = '宝马'
# bmw.run()
# bmw.zhuiwei()
#
# aodi = Car(3, 'black')
# print( ' 奥迪 的内存地址是 %d' % id(aodi) )
# aodi.name = '奥迪'
# aodi.jiao()
# aodi.run()
# aodi.zhuiwei()
