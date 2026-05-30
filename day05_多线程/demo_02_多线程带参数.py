'''
需求:同时运行写代码和听音乐

步骤:
1.导包threading
2.写两个任务函数,写代码和听歌
3.通过多进程类创建对象
4.往对象里传入参数,target传入参数名
5.运行进程
'''
# 1.导包thread
import time
import threading


# 2.写两个任务函数,写代码和听歌
def coding(name, num):
    for i in range(num):
        print(f'{name}在写第{i}行代码...')
        time.sleep(0.5)


def music(name, num):
    for i in range(num):
        print(f'{name}在听第{i}首音乐...')
        time.sleep(0.5)


if __name__ == '__main__':
    coing_thread = threading.Thread(target=coding, args=('韩立', 5))
    muing_thread = threading.Thread(target=music, kwargs={'name': '韩立', 'num': 5})

    # 运行进程
    coing_thread.start()
    muing_thread.start()
