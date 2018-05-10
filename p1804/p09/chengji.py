
'''
成绩 如果 > 60分  ： 合格
如果 成绩 > 85分  ： 优秀
否则  不合格
'''
chengji = float(input("请输入成绩："))

if chengji > 60 and chengji < 85:
    print ("合格")
elif chengji >= 85:
    print ("优秀")
else:
    print ("不合格")

# 当if判断 只有 两种情况的时候
if chengji > 60:
    print ("")
    pass # 占位 字符
else:
    pass

# 当if判断 出现 两种以上的时候
if chengji > 90:
    pass
elif chengji > 80:
    pass
elif chengji > 70:
    pass
elif chengji > 60:
    pass
elif chengji > 50:
    pass
else:
    pass

if chengji > 50 and chengji < 60: # and 同时满足
    print("1")
elif chengji > 70 or chengji < 80:  # or 或者 满足其中一个
    print("2")



