# - 定义登录校验装饰器 `check`。
# - 用原始方式 `comment = check(comment)` 装饰一次。
# - 再用 `@check` 语法糖装饰另一个函数。
# - 对比两种写法并在注释中写出“等价关系”。


# - 定义登录校验装饰器 `check`
def check(fn):
    def inner():
        print('请先登录')
        fn()

    return inner


# 原始方法
def comment():
    print('发表评论')


comment = check(comment)
comment()


# 语法糖
@check
def like():
    print('点赞')


like()
