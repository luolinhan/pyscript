'''
newfile=r'/Users/lhluo/PycharmProjects/pyscript/new1.txt' #指定文件名称和路径
b_new_file=open(newfile,'w')#w模式打开文件 ，可写，a模式，追加
t_n=b_new_file.write('i like iflytek!') #写入对象
b_new_file.close()#关闭文件
print("往文件里写入%d字节内容"%(t_n))提示写入的字节数


newfile=r'/Users/lhluo/PycharmProjects/pyscript/new1.txt' #指定文件名称和路径
b_new_file=open(newfile,'r')#w模式打开文件 ，可写，a模式，追加
tt=b_new_file.read() #读取对象
print(tt)

newfile=r'/Users/lhluo/PycharmProjects/pyscript/new1.txt'
t1=open(newfile,'r')
dd=1
while dd:
    dd=t1.readline()
    print(dd)
'''
import os
import requests
os.system('ifconfig')
