# 创建装饰器
# 1.1 创建闭包,外部函数,传入参数和函数,创建内部函数,引用参数和函数,外部函数返回内部函数名
# 外部
def outer(flag):
    def mindle(function):
        def inner(num1, num2):
            if flag == '+':
                print('正在努力进行运算')
            return function(num1, num2)

        return inner

    return mindle


# 语法糖
@outer('+')
def add(a, b):
    return a + b


print(add(1, 2))
