#-*-coding=utf-8-*-
# 闭包

def funout(out=1):
    outlist = [out]  # 外部函数的变量
    def funin():
        outlist[0] += 1
        print (outlist[0])
    return funin

ain = funout()
print (id(ain))
ain()
ain()
cin = funout()
print (id(cin))
cin()





