'''
闭包的条件
1. 先写外部函数
2. 写外部函数的变量
3. 写内部函数
4. 内部函数引用外部变量
5. 有返回
6. 运行测试
'''


# 1. 先写外部函数
# 2. 写外部函数的变量
def outer(num1):
    # 3.写内部函数
    def inner(num2):
        result = num1 + num2
        return result

    # 5.有返回
    return inner


# 测试
# 首先out的值是返回的inner函数以及保存的outer传入的num1
out = outer(10)
# 等于将第二个参数传入inner,计算result并返回
inner = out(2)
print(inner)
# 又重新到out = outer(10),即返回的inner函数以及保存的outer传入的num1
inner = out(9)
print(inner)
