'''
需求:同时运行写代码和听音乐

步骤:
1.导包multiprocessing
2.写两个任务函数,写代码和听歌
3.通过多进程类创建对象
4.往对象里传入参数,target传入参数名
5.运行进程
'''
# 1.导包multiprocessing
import multiprocessing
import time
import os

# 2.写两个任务函数,写代码和听歌
def coding(num, name):
    for i in range(num):
        print(f'{name}写代码,已经写到第{i+1}行了...')
        time.sleep(2)
    print(f'写代码的进程号:{os.getpid()},父进程号:{os.getppid()}')

def music(count, name):
    for i in range(count):
        print(f'{name}在听第{i+1}首音乐...')
        time.sleep(0.5)
    print(f'听音乐的进程号:{os.getpid()},父进程号:{os.getppid()}')


if __name__ == '__main__':
    coing_process = multiprocessing.Process(target=coding, args=(5, '小明'))
    muing_process = multiprocessing.Process(target=music, kwargs={'count': 5, 'name': '小明'})

    # 运行进程
    coing_process.start()
    muing_process.start()
    print(f'主进程的进程号:{os.getpid()}')

