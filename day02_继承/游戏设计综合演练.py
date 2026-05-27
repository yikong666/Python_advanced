# 定义 `Wallet` 类，要求：
class Wallet:
    # 1. 使用 `__init__` 初始化用户名 `username` 和私有余额 `__balance`。
    def __init__(self, username, balance):
        self.username = username
        self.__balance = balance

    # 2. 定义 `get_balance()` 方法，返回当前余额。
    def get_balance(self):
        return self.__balance

    # 3. 定义 `deposit(money)` 方法，存钱金额必须大于 0。
    def deposit(self, money):
        if money > 0:
            self.__balance += money
        else:
            print('存入金额异常!')

    # 4. 定义 `pay(money)` 方法，付款金额必须大于 0，且不能超过余额。
    def pay(self, money):
        if money > 0 and self.__balance > money:
            self.__balance -= money
        else:
            print('余额不足!')


# 5. 创建对象并测试存钱、付款、余额不足三种情况。
user = Wallet('韩立', 900)
print(user.get_balance())
user.deposit(100)
print(user.get_balance())
user.pay(1100)
print(user.get_balance())
