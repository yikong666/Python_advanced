'''
核心定义:
封装是将对象的属性和方法包裹到类的内部，并可通过权限控制（如私有属性 / 方法）限制外部直接访问，仅暴露指定的公共接口供外部交互。其核心目的是保护数据安全、降低代码耦合度。

关键细节
基础封装：把属性和方法写在类内部（最基础的封装形式），比如把体重属性和跑步/吃东西方法封装到Student类中。

私有控制：通过在属性 / 方法名前加双下划线 __定义私有成员，实现严格的访问限制：
类内部：可自由访问 / 修改私有成员；
类外部：无法直接访问（直接调用会报错），也不会被子类继承；
公共接口：若需外部操作私有成员，需在类内部定义get_xxx（获取）、set_xxx（修改）等公共方法，在方法中可添加校验逻辑（如体重不能为负数）。
'''


class Student:
    def __init__(self, name, weight):
        self.name = name
        self.__weight = weight  # 私有属性,外部无法直接访问

    # 私有方法(体重自检)
    def __check_weight(self):
        if self.__weight < 0:
            self.__weight = 0
            print(f'{self.name}体重异常,已重置为0kg')

    # 公共接口,修改私有属性(带校验)
    def set_weight(self, name, new_weight):
        if new_weight >= 0:
            self.__weight = new_weight
        else:
            print('体重不能为负数!')
        self.__check_weight()  # 调用私有方法检测传入参数是否合规

    # 公共接口:获取私有属性
    def get_weight(self):
        return self.__weight

    # 公有方法:封装行为,跑步减体重
    def run(self):
        self.__weight -= 0.5
        self.__check_weight()
        print(f'{self.name}跑步后体重:{self.__weight}kg')


# 测试封装特性
stu = Student('小明', 75)
print('初始体重:', stu.get_weight())
stu.set_weight('小明', 70)
stu.run()
# stu.set_weight(-5)  # 报错,经私有的体重自检方法检查,传入参数不合规



# 封装的强化案例
# 银行账户
'''
定义BankAccount类，包含私有属性__balance（余额）；
提供公共方法：
deposit(money)：存款（money 需 > 0，否则提示错误）；
withdraw(money)：取款（money 需 > 0 且≤余额，否则提示错误）；
get_balance()：查询余额；
测试：存款 1000 → 取款 500 → 取款 600（提示余额不足）→ 查询最终余额。
'''
class BankAccount:
    def __init__(self):
        self.__balance = 0  # 私有余额,初始为0

    # 公共方法 (存款)
    def deposit(self, money):
        if money > 0:
            self.__balance += money
        else:
            print('存款金额不能为空!')

    # 公共方法(取款)
    def withdraw(self, money):
        if money > 0 and self.__balance>=money:
            self.__balance -= money
        else:
            print('取款金额异常#!')

    # 查询余额
    def 






