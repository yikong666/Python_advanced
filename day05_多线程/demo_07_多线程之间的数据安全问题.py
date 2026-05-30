'''
1.导包
2.定义两个函数
3.定义两个函数
4,创建线程
5.启动线程
'''



import threading

# 2.定义两个函数
g_num = 0

# 3.定义两个函数
def sum_num1():
    for i in range(1000000):
        global g_num
        g_num += 1
    print('sum1:', g_num)

def sum_num2():
    for i in range(1000000):
        global g_num
        g_num += 1
    print('sum2:', g_num)

if __name__ == '__main__':
    # 4.创建子线程
    sum1 = threading.Thread(target=sum_num1)
    sum2 = threading.Thread(target=sum_num2)

    sum1.start()
    sum2.start()
