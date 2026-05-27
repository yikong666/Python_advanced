# 案例一,减肥案例
class Student:
    def __init__(self, name, weight):
        self.name = name
        self.current_weight = weight

    # 跑步方法:
    def run(self):
        self.current_weight -= 0.5  # 状态改变
        print(f'{self.name}去跑步了,减重0.5kg,当前体重为{self.current_weight}kg')

    # eat方法
    def eat(self):
        self.current_weight += 2  # 状态改变
        print(f'{self.name}大吃了一顿,增加2kg,当前体重为:{self.current_weight}kg')


# 测试验证
student = Student('小明', 75)
student.run()
student.eat()


# 案例二
# 烤地瓜
# 用户按意愿设定烤制时间，
# 系统判断状态（0-3分生的，3-7分半生不熟，7-12分熟，>12分糊）；
# 用户可添加调料。要求能直接打印地瓜状态。
class SweetPotato(object):
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 7:
            self.cook_state = '半生不熟'
        elif 7 <= self.cook_time < 12:
            self.cook_state = '熟了'
        else:
            self.cook_state = '已烤焦,糊了'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'总时长:{self.cook_time}分钟  |  状态:{self.cook_state}  |  调料:{self.condiments}'


# 测试试验
potato = SweetPotato()
potato.cook(2)  # 先烤2分钟
print(potato)
potato.cook(6)  # 再烤6分钟,总时长8分钟
print(potato)
potato.add_condiments('辣椒面')
potato.add_condiments('蚝油')
print(potato)
