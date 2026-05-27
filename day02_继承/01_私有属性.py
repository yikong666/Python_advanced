class Girl:
    def __init__(self,name):
        self.name = name
        self.__age =18

    def __show(self):
        print(f'{self.name}今年{self.__age}岁了')



xiaohong = Girl('小红')

print(xiaohong.name)

xiaohong.__show()