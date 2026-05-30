"""
需求：创建生成器，通过推导式的方式完成
(生成数据的公式)

步骤：
1.创建生成器
`2.用next获取生成器的下一个值
3.用for循环遍历每一个值
"""

# 1.创建生成器
my_generator = (i*2 for i in range(5))
print(my_generator)
print(type(my_generator))

# # 2.用next获取生成器的下一个值
# value = next(my_generator)
# print("next：",value)
#
# value = next(my_generator)
# print("next：",value)
#
# value = next(my_generator)
# print("next：",value)
#
# value = next(my_generator)
# print("next：",value)
#
# value = next(my_generator)
# print("next：",value)

#3.用for循环遍历每一个值
for value in my_generator:
    print("for循环：",value)
