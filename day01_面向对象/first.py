#定义汽车类
# class Car:
#     # 无参数，类内部直接赋值
#     def __init__(self):
#         self.car_type = 'suv'
#         self.color = '红色'
#
#     # 内部调用属性
#     def shuxing(self):
#         print(self.car_type)
#         print(self.color)
#
#     # 行驶方法
#     def run(self):
#         print(f'一辆{self.color}的{self.car_type}跑起来了')
#
#     # 停止方法
#     def stop(self):
#         print(f'它停下来了')
#
#     # 内部调用方法
#     def xingshi(self):
#         self.run()
#         self.stop()
#
#     # self关键字测试
#     def test(self):
#         print(f'self 的地址:{self}')
#         print(f'self的整数地址：{id(self)}')

# class WashingMachine(object):
#     # 洗方法
#     def wash(self):
#         print('洗衣机开始洗衣服了')


# wm = WashingMachine()
# wm.wash()

# self关键字的认识
# hongqi = Car()
# hongqi.test()
# print(f'红旗的地址：{hongqi}')
# print(f'红旗的地址:{id(hongqi)}')
#
# changcheng = Car()
# changcheng.test()
# print(f'长城的地址：{changcheng}')
# print(f'长城的地址：{id(changcheng)}')

# car = Car()
# car.shuxing()
# car.run()
# car.stop()
# car.xingshi()






