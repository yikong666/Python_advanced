class Animal:
    def call(self):
        print('动物发出了叫声')


class Dog(Animal):
    def call(self):
        print('狗发出了汪汪叫')


class Cat(Animal):
    def call(self):
        print('猫发出了喵喵叫')


class Car():
    def call(self):
        print('汽车发出滴滴声')


class Train():
    def call(self):
        print('火车发出哐当哐当声')


class Ship():
    def call(self):
        print('汽车发出呜呜声')


# def do(obj):
#     obj.call()
def do(obj):
    if isinstance(obj, Animal):
        obj.call()
    else:
        print('警告,非动物类不能叫')

animal = Animal()
dog = Dog()
cat = Cat()


car = Car()
train = Train()
ship = Ship()
# for i in (car, train, ship):
#     do(i)
for i in (animal, dog, cat, car, train, ship):
    do(i)