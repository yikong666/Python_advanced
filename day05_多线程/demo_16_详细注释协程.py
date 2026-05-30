import asyncio
import time

# async 关键字让这个函数变成一个“协程函数”（coroutine function）
# 调用它不会立即执行里面的代码，而是返回一个“协程对象”（coroutine object）
# 只有被事件循环调度时，协程里的代码才会执行
async def hello(name):
    print(f"[{time.time():.2f}] Hello: {name}")     # 打印开始信息，加上时间戳方便观察
    # await 后面跟一个“可等待对象”（比如协程、任务、Future）
    # asyncio.sleep(1) 不是真的阻塞 1 秒，而是“告诉事件循环：我要等 1 秒，这期间你可以去干别的事”
    await asyncio.sleep(1)
    print(f"[{time.time():.2f}] Goodbye: {name}")

async def main():
    # -------------------------------------------
    # 第一种：顺序等待 (没有并发)
    # -------------------------------------------
    # 直接 await 一个协程，相当于 “我就在这里等你完全结束，才继续往下走”
    await hello("Alice")  # 当前协程在这里暂停，直到 hello("Alice") 彻底执行完
    print("---------")

    # -------------------------------------------
    # 第二种：并发执行 (真正的异步)
    # -------------------------------------------
    # asyncio.create_task() 把协程包装成一个 Task（任务），并立即提交给事件循环
    # “提交”意味着：事件循环已经开始调度这个任务了，不会等你去 await 它
    task1 = asyncio.create_task(hello("Bob"))
    task2 = asyncio.create_task(hello("Charlie"))

    # 两个任务现在都已经在事件循环里“跑起来”了
    # 此时 main() 还没结束，后面用 await 只是“等待任务完成”，但任务之间已经在并发运行了
    await task1  # 等待 task1 彻底完成
    await task2  # 等待 task2 彻底完成
    # 注意：即便这里只 await task1，task2 其实也已经在后台运行了

# 程序入口
# asyncio.run(main()) 会创建一个事件循环，把 main() 这个协程放进去跑，直到它结束
asyncio.run(main())