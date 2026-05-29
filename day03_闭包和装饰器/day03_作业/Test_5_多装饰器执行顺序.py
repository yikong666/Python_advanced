# - 定义两个装饰器 `deco1`、`deco2`，分别打印“前/后”日志。
# - 同时装饰一个函数，观察执行顺序。
# - 用注释写清楚：谁先装饰、谁先执行。
def deco1(fn):
    def inner():
        print("deco1 前")
        fn()
        print("deco1 后")
    return inner

def deco2(fn):
    def inner():
        print("deco2 前")
        fn()
        print("deco2 后")
    return inner

@deco1
@deco2
def work():
    print("原函数执行")

work()