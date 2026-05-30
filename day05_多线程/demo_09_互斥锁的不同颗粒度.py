import threading   # 导入线程模块，用于创建和管理线程
import time        # 导入时间模块，用于模拟耗时操作和计时

count = 0          # 全局变量，模拟“炒好的菜的数量”，多个线程会同时修改它
lock = threading.Lock()  # 创建一把互斥锁，模拟“灶台”——同一时刻只有一个线程能使用


# ---------- 方案A：粗粒度锁（进门就反锁整个厨房） ----------
def task_coarse():
    global count                # 声明要修改全局变量 count
    for _ in range(50):         # 每个线程做 50 道菜
        lock.acquire()          # ① 获取锁（相当于进门立刻反锁厨房）
        time.sleep(0.01)        # ② 模拟洗菜耗时 0.01 秒，此时锁仍然被持有
        count += 1              # ③ 模拟炒菜（只有这一步真正需要互斥）
        lock.release()          # ④ 释放锁（全部干完才开门）
    print(f"方法A计数为：{count}")  # 打印本线程完成后的 count（非最终值）


# ---------- 方案B：细粒度锁（只锁灶台） ----------
def task_fine():
    global count                # 声明全局变量
    for _ in range(50):         # 每个线程做 50 道菜
        time.sleep(0.01)        # ① 模拟洗菜——注意：这一步在锁外！多个线程可以同时洗

        lock.acquire()          # ② 真正要动锅铲（修改共享变量）时才抢锁
        count += 1              # ③ 模拟炒菜（临界区，必须互斥）
        lock.release()          # ④ 炒完立刻释放锁，不占着灶台
    print(f"方法B计数为：{count}")


# ---------- 统一的测试启动逻辑 ----------
def run_test(func, name):
    global count
    count = 0                      # 每次测试前把菜数归零
    start = time.time()            # 记录开始时间

    # 创建两个线程，都执行同一个任务函数
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)

    t1.start()                     # 启动线程1
    t2.start()                     # 启动线程2

    t1.join()                      # 等待线程1结束
    t2.join()                      # 等待线程2结束

    # 打印测试结果：方案名、总耗时、最终做菜数（理论上应为100）
    print(f"{name} | 耗时: {time.time() - start:.2f} 秒 | 最终做菜数: {count}")


# ---------- 运行对比 ----------
if __name__ == "__main__":
    run_test(task_coarse, "【粗锁】")   # 先测试粗粒度锁
    run_test(task_fine, "【细锁】")     # 再测试细粒度锁