class Girl:
    def __init__(self,name):
        self.name = name
        self.__age =18

    def __show(self):
        print(f'{self.name}今年{self.__age}岁了')

    # 设置get方法
    def get_age(self):
        return self.__age
    # 设置set方法
    def set_age(self, age):
        self.__age = age


xiaohong = Girl('小红')
print(xiaohong.get_age())
xiaohong.set_age(23)
print(xiaohong.get_age())

