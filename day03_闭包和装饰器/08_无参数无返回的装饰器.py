'''
定义一个装饰器,他们都没有参数,没有返回
'''
# 步骤
# 1 定义闭包
def outer(function):
    # 定义一个内部函数
    def inner():
        print('正在计算中')
        function()
    return inner
# 使用语法糖
@outer
# 定义原函数
def ori():
    a = 10
    b = 20
    print(f'两数之和{a + b}')

ori()