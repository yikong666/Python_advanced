'''

'''
# 1. 导包
import time
import threading

#2.写函数
def get_info():
    time.sleep(0.4)
    #打印线程信息
    current_thread = threading.current_thread()
    print(current_thread)

#3.写循环,创建线程
if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_info)
        sub_thread.start()