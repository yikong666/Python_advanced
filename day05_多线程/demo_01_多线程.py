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
def coding():
    for i in range(3):
        print('写代码...')
        time.sleep(2)

def music():
    for i in range(3):
        print('听音乐...')
        time.sleep(2)

if __name__ == '__main__':
    coing_thread = threading.Thread(target=coding)
    muing_thread = threading.Thread(target=music)

    # 运行进程
    coing_thread.start()
    muing_thread.start()











