# 1.创建类
class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入钱数')
    def __take_money(self):
        print('取钱')
    def __print_bill(self):
        print('打印账单')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__take_money()
        self.__print_bill()

user1 = ATM
user1.withdraw()

