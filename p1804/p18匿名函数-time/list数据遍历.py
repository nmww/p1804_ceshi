
# 遍历
l_name = [{'号码':110,'姓名':'张三'},{'号码':119,'姓名':'李四'}]

haoma = int(input('请输入号码'))

flag = 0  # 记号 标记 表示
for i in l_name:
    if i['号码'] == haoma:
        print ('存在')
        flag = 123   # 设定 标记 为 1
        break

if flag == 0:
    print ('没找到')
elif flag == 123:
    print ('存在')







