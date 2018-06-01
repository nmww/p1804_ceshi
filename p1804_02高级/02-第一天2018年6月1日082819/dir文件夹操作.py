
# python对于文件夹的操作
import os

# 创建文件夹
#os.mkdir('house')  # 当前路径，创建 文件夹
#os.mkdir('../girl') #  相对或绝对路径，+ 文件夹

# pwd
p = os.getcwd()  #得到当前的路径
print ('当前的路径是： %s' % p)


# 修改默认的路径 change
os.chdir('./house')
print ('修改之后的默认路径是：%s' % os.getcwd())

f = open('1.txt','w')

#os.mkdir('xiaohua')  #  创建到了新的路径下

#os.rmdir('xiaohua')

os.chdir('../')
# OSError: [Errno 39] Directory not empty: 'house'
# os.rmdir('house')
# 当文件夹空的时候，可以用 os.rmdir 删除
# 当文件夹不空的时候  用  以下方法删除
import shutil
shutil.rmtree('house')




