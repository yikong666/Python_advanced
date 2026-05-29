# **任务要求：**
# 定义外部函数 `func_out(num1)`，内部函数 `func_inner(num2)`。
# 内部函数使用外部变量完成求和并打印。
# 外部函数返回内部函数，创建闭包并调用。
# 解释每一行如何对应“有嵌套/有引用/有返回”三条件。


# 定义外部函数 `func_out(num1)`，内部函数 `func_inner(num2)`。
def func_out(num1):
    def func_inner(num2):
        result = num1 + num2
        # 内部函数使用外部变量完成求和并打印。
        print(f'求和结果为:{result}')

    # 外部函数返回内部函数，创建闭包并调用。
    return func_inner

f_o = func_out(1)
f_o(5)
