"""
需求：使用yeild方式来创建生成器，并运行查看结果

步骤
1.创建一个函数
2.创建一个循环
3.使用yeild运行
4.生成对象，使用生成器
"""

# 1.创建一个函数
def my_generator(n):
    # 2.创建一个循环
    for i in range(n):
        print("开始生成")
        # 3.使用yeild运行
        yield i
        print("结果为：",i)
        print("完成了一次")

# 4.生成对象，使用生成器
my_gen = my_generator(3)
# result = next(my_gen)
# print(result)
# result = next(my_gen)
# print(result)
# result = next(my_gen)
# print(result)

for value in my_gen:
    print(value)