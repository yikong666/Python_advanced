import threading
import time


# 创建函数
def work():
    for i in range(10):
        print('工作中...')
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建子线程
    work_thread = threading.Thread(target=work)
    # 第一种方式:守护主线程
    # work_thread = threading.Thread(target=work, daemon=True)
    # 第二种方式
    work_thread.daemon = True
    # 启动子线程
    work_thread.start()

    time.sleep(1)
    print('主线程运行完毕')
