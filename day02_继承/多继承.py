class Father:
    def __init__(self, leg):
        print('继承自父亲')
        self.leg = leg


class Mother:
    def __init__(self, leg):
        print('继承自母亲')
        self.leg = leg


class Child(Father, Mother):
    print('孩子开始继承')

    def __init__(self, leg):
        # self.leg = leg
        # Mother.__init__(self,leg)
        super().__init__(leg)


child = Child('大长腿')
print(Child.mro())
