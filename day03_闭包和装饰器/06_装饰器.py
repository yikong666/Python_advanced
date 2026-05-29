'''
创建一个装饰器使用传统方法装饰原函数
在不改变原函数内部情况下,给其内部增加额外的功能
'''
# 1 创建一个闭包,有特殊功能,形成一个装饰器
def outer(function):
    # 创建一个内部函数
    def inner():
        # 有额外功能
        print('登录验证...')
        function()
    # 有返回
    return inner

# 创建原函数
def ori():
    print('发表评论')

commet = outer(ori)
commet()