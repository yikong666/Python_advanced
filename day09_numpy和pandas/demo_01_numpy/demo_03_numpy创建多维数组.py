# 1.导包
import numpy as np

# 2.创建一维数组(array函数)
arr1 = np.array([1, 2, 3, 4, 5])
print(type(arr1))
print(arr1)

# 3.创建二维数组
arr2 = np.array([[1, 2, 5], [3, 4, 5]])
print(type(arr2))
print(arr2)
print('-' * 30)

# 4.创建全0数组(zeros函数)
zero_arr = np.zeros((3, 4))  # 后加括号3代表一维有3个元素,4代表二维有两个元素
print(zero_arr)

# 全1数组,且多唯(全0数组)
ones_arr = np.zeros((2, 3, 1, 2))
print(ones_arr)

# 5.创建序列数组(范围数组函数arange)
range_arr = np.arange(0, 10, 2)  # 左闭右开,步长为2
print('范围数组:', range_arr)

range_arr_sim = np.arange(0, 10)
print('范围函数简单:', range_arr_sim)

# 6.创建等分数组（linspace）
# 除以n-1,分为n-1个段落
linspace_arr = np.linspace(0, 10, 5)
print('等分数组:', linspace_arr)

# 7.创建随机数组
# 0-1分布
random_arr = np.random.rand(3, 3)
print(random_arr)

# 正态分布
normal_arr = np.random.randn(3, 3)
print(normal_arr)


