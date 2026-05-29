"""
需求：创建一个什么形式都能接受的装饰器，任何参数形式的原函数，都能进行装饰
关键点：*args,**kwargs,return
步骤：
1.创建一个装饰器
    创建外部函数，引用函数，创建内部函数，调用外部函数，返回，额外的功能
2.把万能参数装进去，里面加上return
3.创建4种不同参数类型的原函数，无无，有无，无有，有有
4.用装饰器，装饰这些原函数，使用语法糖方法
5.调用原函数
"""

# 1.创建一个装饰器
def outer(function):
    # 2.把万能参数装进去，里面加上return
    # *args,**kwargs保证匹配任何形式
    def inner(*args, **kwargs):
        bag = function(*args, **kwargs)
        #加一个额外的功能
        done_bag = f"打包好了内含:\n{bag}"
        #交给快递员
        return done_bag
    return inner

# 3.创建4种不同参数类型的原函数，无无，有无，无有，有有

#无参数无返回
@outer
def nono():
    print("把信放入快递箱")

#有参数无返回
@outer
def yesno(book_name):
    print(f"正在打包{book_name}")

#无参数有返回
@outer
def noyes():
    return f"我已经把包裹放进来了"

#有参数有返回
@outer
def yesyes(cup_name):
    return f"{cup_name}容易碎，请轻拿轻放"

#任意形式
@outer
def freedom(*items,person_name="匿名"):
    return f"物品清单：{items},寄件人：{person_name}"

# 5.调用原函数
print("=====开始了=====")
print(nono())

print(yesno("《python从入门到精通》"))

print(noyes())

print(yesyes("瓷杯子"))

print(freedom("键盘","鼠标","坦克","飞机",person_name="张三"))