'''
1.导包
2.定义全局变量
3.创建锁
4.定义两个函数
5.上锁,解锁
6.创建子线程,传参
7.启动线程,
'''



import threading

# 2.定义两个函数
g_num = 0
# 3.创建锁
mutex = threading.Lock()
# 4.定义两个函数
def sum_num1():
    # 上锁
    mutex.acquire()
    for i in range(1000000):

        global g_num
        g_num += 1
    # mutex.release()
    print('sum1:', g_num)

def sum_num2():
    # 上锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    # mutex.release()
    print('sum2:', g_num)

if __name__ == '__main__':
    # 4.创建子线程
    sum1 = threading.Thread(target=sum_num1)
    sum2 = threading.Thread(target=sum_num2)

    sum1.start()
    sum2.start()
 