### 1. 定义学生类

# 定义 `Student` 类，要求：
#
# 1. 使用 `__init__` 初始化 `name` 和 `age`。
# 2. 定义 `introduce()` 方法，输出学生姓名和年龄。
# 3. 创建两个学生对象，分别调用 `introduce()`。
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'姓名为:{self.name},年龄为:{self.age}')
stu1 = Student('小明', 22)
stu1.introduce()
stu2 = Student('小帅', 23)
stu2.introduce()





### 2. 定义手机类并打印对象信息

# 定义 `Phone` 类，要求：
#
# 1. 使用 `__init__` 初始化 `brand` 和 `price`。
# 2. 定义 `call()` 方法，输出“某品牌手机正在打电话”。
# 3. 定义 `__str__()` 方法，打印对象时显示品牌和价格。
# 4. 创建两个手机对象并测试。
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    # 打电话方法
    def call(self):
        print(f'正用{self.brand}正在打电话')
    def __str__(self):
        return f'品牌为{self.brand},价格为:{self.price}'

iphone = Phone('苹果', 8999)
print(iphone)
iphone.call()
xiaomi = Phone('小米', 4999)
print(xiaomi)
xiaomi.call()



### 3. 封装账号余额

# 定义 `Account` 类，要求：
#
# 1. 使用 `__init__` 初始化用户名和私有余额 `__balance`。
# 2. 定义 `get_balance()` 方法，返回余额。
# 3. 定义 `deposit(amount)` 方法，充值金额。
# 4. 创建对象并测试充值前后余额。
class Account:
    def __init__(self, balance):
        self.__balance = balance

    # 2. 定义 `get_balance()` 方法，返回余额
    def get_balance(self):
        print(f'余额为:{self.__balance}')

    # 3.定义充值金额
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('金额输入错误')
user = Account(10)
user.get_balance()  # 10
user.deposit(90)
user.get_balance()  # 100




