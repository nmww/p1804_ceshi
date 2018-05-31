
# 铁锅炖鱼

def cookFish():
    ''' 炖鱼的详细 步骤 '''
    print ("1. 买鱼 or 钓鱼;")
    print ("2. 杀鱼 ；")
    print ("3. 洗，料酒胭脂;")
    print ("4. 点火，下锅.")
    print ("5. 到点，出锅。")
    print ("6. 小二 上菜")
    print ("7. 洗手 吃饭。")

def cookCaoFan():
    ''' 炖鱼的详细 步骤 '''
    print ("1.点火;")
    print ("2. 加饭 ；")
    print ("3. 加蛋")
    print ("4. 搅拌.")
    print ("5. 齐活儿，开吃。")


#-------------------------------

diancai = input ("你要吃啥:")
if diancai == 'yu':
    cookFish()
elif diancai == 'fan':
    cookCaoFan()



