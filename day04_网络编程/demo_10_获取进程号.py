import multiprocessing
import os

# 获取当前进程号
pid = os.getpid()
print(pid)


pid = multiprocessing.current_process().pid
print(pid)

ppid = os.getppid()
print(ppid)