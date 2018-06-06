#-*-coding:utf-8-*-

# 买房子    家具 （床，沙发）
#  两个类  1. 房子 2. 家具
class House:  # 定义 房子类
    def __init__(self, area, addr,):
        self.area = area
        self.addr = addr
        self.items = []
    def __str__(self):
        return "新房子的大小是 %d , 地址位于：%s， 其中包含的家具有：%s" % (self.area, self.addr, str(self.items))

    def add_items(self, item):  #添加家具
        if self.area > item.area:
            #self.area -= item.area
            self.items.append(item.name)
        else:
            print ('家具太大了，我小小的家，容纳不下。')

class Bed:  #定义 床类
    def __init__(self, area, name):
        self.area = area
        self.name = name
    def __str__(self):
        return "%s 已经购买好了，他的大小是%d" % (self.name, self.area)

house01 = House(200, '前门北大大街01号')
print( house01 )
baby_bed = Bed(100,'婴儿床')
print(baby_bed)
house01.add_items(baby_bed)
print( house01 )

sr_bed = Bed(90,'双人席梦思软床')
house01.add_items(sr_bed)
print( house01 )

big_bed = Bed(100,'巨人专用平板床')
house01.add_items(big_bed)
print( house01 )
