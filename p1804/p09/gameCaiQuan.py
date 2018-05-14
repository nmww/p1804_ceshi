
'''
这是一个美女机器人，猜拳小游戏
石头：1   剪刀：2  布：3
pc = 1
user = input 2


#-----user win
if user == 1 and pc == 2:
    print uesr win
elif user == 2 and pc == 3:
    print user win
elif user == 3 and pc == 1:
    print user win

if (u==1 and pc ==2) or u==2 and pc==3 or u==3 and pc==1:
    print  u win
#-----user == pc
if user == pc
    pingju
#----- pc win
    print  loser

'''
# random 使用  1. 导入包 import
# random 使用  2. 获取随机整数 random.randint(1,100)
import random


userInput = 'begin'

while userInput=='begin': # True

	# 拳头：1  剪刀 ：2 布： 3
	shitou = '石头' #定义 变量 shitou 保存文件内容 石头
	jiandao = '剪刀'
	bu = '布'
	#user = int(input("请用户出小拳拳："))  # 1; 3
	# user 代表用户输入的 拳脚
	user = input("请用户出小拳拳：") # 直接输入 石头 剪刀 布
	if user == 'q':
            break
	    #userInput = 'q'
	# pc 代表计算机 随机出来的 整数
	pc = random.randint(1,3) # 2; 3
	#print ("美女电脑出了：%d " % pc)
	# 美女随机1 显示 拳头; 依次类推
	# 根据计算机随机出来的整数 定义好 计算机对应的 拳脚
	if pc == 1:
	    pcStr = shitou
	    print("美女电脑出了:石头")
	elif pc == 2:
	    pcStr = jiandao
	    print("美女电脑出了:-剪刀")
	else:
	    pcStr = bu
	    print("美女电脑出了:布")

	if (user==shitou and pcStr==jiandao) or (user==jiandao and pcStr==bu) or (user==bu and pcStr==shitou):
	    print ("电脑太弱了…………")
	elif user == pcStr:
	    print ("心有灵犀…… 咱俩再来过……")
	else:
	    print ("你太笨了……")





