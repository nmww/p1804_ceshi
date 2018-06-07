import time,random

def RowColumnsRandom(rcNum, pNum):
    list = []
    while True:
        i = random.randint(1,rcNum)
        if i in list:
            time.sleep(2)
            print('正在思考，不要着急哦……………………')
        else:
            if len(list) == pNum:
                break
            else:
                list.append(i)
    return list

print(' >>>>>>> ARE YOU READY? GO GO GO !! <<<<<<<'.center(60,'-'))
#time.sleep(3)
pNum = 3
rowList = RowColumnsRandom(5, pNum)
print(' [ 行 ] 已经选择好了现在开始选择 [ 列 ] 了……………………')
#time.sleep(3)
columnsList = RowColumnsRandom(7, pNum)
print(' [ 列 ] 已经选择好了，准备揭晓答案……………………')
#time.sleep(1)
for i in range(0,pNum):
    if (columnsList[i]==1) and (rowList[i] > 4):
        print('第 [ %d ] 幸运星是，从左向右：第【%d】列，第【3】行！' % (i, columnsList[i]))
    elif (columnsList[i]==5) and (rowList[i] > 4):
	    print('第 [ %d ] 幸运星是，从左向右：第【%d】列，第【4】行！' % (i, columnsList[i]))
	#elif (columnsList[i]==6) and (rowList[i] > 4):
	#	print('第 [ %d ] 幸运星是，从左向右：第【%d】列，第【4】行！' % (i, columnsList[i]))
	#elif (columnsList[i]==7) and (rowList[i] > 4):
	#	print('第 [ %d ] 幸运星是，从左向右：第【%d】列，第【4】行！' % (i, columnsList[i]))
    else:
        print('第 [ %d ] 幸运星是，从左向右：第【%d】列，第【%d】行！' % (i, columnsList[i], rowList[i]))
    time.sleep(1)
print(' ----->>>>>>> WELCOME : COME ON BABY <<<<<<<-------')