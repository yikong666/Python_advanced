# 创建装饰器
# 1.1 创建闭包,外部函数,传入参数和函数,创建内部函数,引用参数和函数,外部函数返回内部函数名
# 外部
def outer(function, flag):
    def inner(num1, num2):
        if flag == '+':
            print('正在努力进行运算')
        return function(num1, num2)

    return inner


def add(a, b):
    return a + b


add = outer(add, '+')
result = add(1, 3)
print(result)
