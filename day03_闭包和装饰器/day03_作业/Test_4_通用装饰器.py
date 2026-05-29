# - 编写一个通用装饰器，内部函数使用 `*args, **kwargs`。
# - 要求可装饰四类函数：
#   1) 无参无返回
#   2) 有参无返回
#   3) 无参有返回
#   4) 有参有返回（含关键字参数）
# - 演示调用结果，证明“参数和返回值都不丢失”。

def outer(func):
    def inner(*args, **kwargs):
        print('通用装饰器测试')
        result = func(*args, **kwargs)
        return result
    return inner

#   1) 无参无返回
def nono():
    print('无参无返回')

nono = outer(nono)
nono()


#   2) 有参无返回
@outer
def yesno(a, b):
    c = a+b
    print(f'有参无返回,求和:{c}')

yesno(1, 4)



#   3) 无参有返回
@outer
def noyes():
    return '无参有返回'
print(noyes())



#   4) 有参有返回（含关键字参数）
@outer
def yesyes(a, b):
    c = a + b
    print(f'有参有返回,求和:{c}')
    return c

yesyes(1, 4)