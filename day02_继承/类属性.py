'''
步骤
1 创建类
2 定义一个类属性
3 对类属性进行修改计数
4 设置一个通用类属性
5 创建三个对象
6 观察类属性的变化
'''


# 1 创建类
class Tools(object):
    # 定义一个类属性
    count = 0
    cls_name = '工具'

    def __init__(self, name):
        self.name = name
        # 计数
        Tools.count += 1


tool1 = Tools('斧头')
print(Tools.count)
tool2 = Tools('扳手')
print(Tools.count)
tool3 = Tools('螺丝刀')
print(Tools.count)

print(tool1.count)
print(tool2.count)
print(tool3.count)
