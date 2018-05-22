
'''
1. 添加菜单
2. 查询全部菜单
3. 查询一个指定菜单
4. 点餐
5. 结帐
6. 推出
'''
# 定义变量保存 菜单
cd_list = []  #定义一个空列表
'''
dic
菜名：土豆丝
价格：12元
类型：素材
口味：酸辣
'''
def c_menu():
    print ("-"*20)
    print ('欢迎是如家菜馆点菜系统')
    print ('1. 添加菜')
    print ('2. 查询全部')
    print ('3. 退出')
    print ('4. 点参')
    print ('5. 结帐')
    print ("-"*20)

def add_cd():
    c_name = input("请输入菜品名称：")
    c_price = input("请输入菜品价格：")
    c_class = input("请输入菜品类型：")
    c_wei = input("请输入菜品口味：")
    cd_dic = {}  # 把输入的内容保存到字典里 ，只是一个菜
    cd_dic["c_name"] = c_name
    cd_dic["c_price"] = c_price
    cd_dic["c_class"] = c_class
    cd_dic["c_wei"] = c_wei
    cd_list.append(cd_dic) # 把这一个菜添加到  列表菜单中。

def s_all():
    if len(cd_list) > 0:
        a = 1
        for i in cd_list:
            print ('%d:您选的菜名是：%s, 价格是 %s,类型是%s,口味是：%s' % (a,i['c_name'],i['c_price'],i['c_class'],i['c_wei']) )
            a += 1


js_list = []
def diancan(n):
    dic = cd_list[n-1]
    js_list.append(dic)  # 最后结帐使用，客户点了声明菜
    return dic  #返回给调用这 一个字典， 保存了菜的完整信息
def jiezhang():
    '''结帐计算金额'''
    s = 0
    if len(js_list)>0:
        for i in js_list:
            s += int(i['c_price'])

    return s

while True:
    c_menu()
    n = int(input('请输入您需要的操作：'))
    if n == 1:
        add_cd()
    elif n==2:
        s_all()
    elif n==3:
        break
    elif n==4:
        x = int(input('请输入您要点菜的编号：'))
        d = diancan(x)  #返回的是一道菜的完整信息， 字典类型中
        print ('您选的菜名是：%s, 价格是 %s'% (d['c_name'],d['c_price']))
    elif n==5:
        s = jiezhang()
        print ('您本此应当支付金额是%d'% s)

    else:
        print('请按照套路出牌')

