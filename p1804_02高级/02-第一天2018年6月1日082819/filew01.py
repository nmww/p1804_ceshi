# -*- coding=utf-8 -*-
# 文件的简单读写



f = open('61活动方案.txt','w+')
f.write('今天是6月1日儿童节，穿什么显得年轻;\n')
f.write('穿，开裆裤，最年轻\n')
f.close()
f = open('61活动方案.txt','r')

#f = open('61活动方案.txt','w')
#f.write('哈哈哈哈哈哈\n')

#f.write('aaaa')

content = f.read()
print (content)

f.close()
