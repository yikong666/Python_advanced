'''
查看多进程之间数据是否隔离,会不会共享

步骤
1.导包
2.创建一个全局变量
3.写两个函数
4.创建两个子进程
5.执行进程查看结果
'''

# 1.导包
import time
import multiprocessing

# 2.创建一个全局变量
my_list = []

def write_data():
    for i in range(5):
        my_list.append(i)
        print(f'增加了{i}')
    print('write写入后:',my_list)

def read_data():
    print('read读取后:',my_list)

if __name__ == '__main__':
    write_process = multiprocessing.Process(target=write_data)
    read_process = multiprocessing.Process(target=read_data)

    write_process.start()
    read_process.start()