class Animal:
    def call(self):
        print('动物发出了叫声')

class Dog(Animal):
    def call(self):
        print('狗发出了汪汪叫')

class Cat(Animal):
    def call(self):
        print('猫发出了喵喵叫')

def do(obj):
    obj.call()

animal = Animal()
dog = Dog()
cat = Cat()
for i in (animal, dog, cat):
    do(i)
