#-*-coding:utf-8-*-

# 拳皇各种角色
class People:
    def __init__(self, name, heigh, weight):
        self.name = name
        self.heigh = heigh
        self.weight = weight
    def jump(self):
        print('%s 跳起来了……' % self.name)
    def run(self):
        print("%s 跑起来……" % self.name)
    def zhiquan(self):
        print("%s 直拳……" % self.name)
    def tang(self):
        print('%s 躺下开始装死……' % self.name)

chengguohan = People('程国汉','2.50米',250)
chengguohan.jump()

caotijing = People('草薙京','1.80米',160)
caotijing.jump()


