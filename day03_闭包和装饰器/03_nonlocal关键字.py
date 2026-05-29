# nonlocal: 声明能够让内部函数去修改外部函数的变量
def fun_out():
    a = 100
    def func_inner():
        # 声明变量
        nonlocal a
        a += 1
        print(f'修改的结果{a}')
    return func_inner

number = fun_out()
number()