# 获取 输入的价格
xgPrice = input("请您输入西瓜的价格：")
# 获取 输入的重量
xgWight = input("请您输入西瓜的重量：")

#-------------------------
# 把输入的 str类型 数据 转化成 int 进行 计算
price = float(xgPrice)
wight = float(xgWight)
# 赋值
priceXG = float( input("请输入西瓜价格:") )
# 计算西瓜的总金额
# money = xgPrice * xgWight
money = price * wight
print ("该西瓜的单价是 %.2f 元/斤 " % (price) )
print ("该西瓜的重量是 %.2f 斤 " % (wight) )
print ("您应当支付总金额是 %.2f 元 " % (money) )

