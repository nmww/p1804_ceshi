#coding=utf-8

# 元类  : 创建类   type
#1.type 创建 类
#  type(类的名称, (类继承对象),{属性})
#Test2 = type("Test2",(),{})  # 定了一个Test2类
#t = Test2()
#print ('类的打印结果：', Test2)
#print ('类对象的打印结果：', t)

#2.type 属性类
#   {'属性名称':属性值}
#Foo = type('Foo', (), {'bar':True, 'b':'你好薄利'})
#print ('类名打印：',Foo)
#print ('类名直接访问属性：',Foo.bar)
#f = Foo()
#print ('类的对象打印：',f)
#print ('类对象访问属性：',f.bar)
#print ('类对象访问属性：',f.b)

#3.type 带函数类  方法
Foo = type('Foo', (), {'bar':True})
#print (Foo)

def echo_bar(self):
    print(self.bar)

#让FooChild类中的echo_bar属性，指向了上面定义的函数
FooChild = type('FooChildName', (Foo,), {'echo_bar1': echo_bar})

b = FooChild()
print(b)
print(b.__class__)
#print(b.bar)
#print(b.echo_bar1())
#print(b.echo_bar1)



