
#  游戏 日常任务循环
'''
1. 签到
2. 采药草
3. 帮助小红帽 找大灰狼
'''

renwu = 1
while renwu <= 3:
    if renwu == 1:
        print ("赶快去签到 领媳妇")
    elif renwu == 2:
        print ("师傅要你去采集 20 个草药！")
        caoyao = 0
        while caoyao <= 20:
            print ("弯腰，提臀，收复，吸气： 开始采集：第 %d 草药"% caoyao)
            caoyao = caoyao +1
    else:
        print ("帮助小红帽 找 大灰狼;")
    renwu = renwu+1



