class Phone(object):
    # 手机的四个属性
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.ispower_on = False  # 默认关机

    def __str__(self):
        return '手机品牌是' + self.brand + ',型号是' + self.model +',价格为:' + str(self.price) + ',颜色是' + self.color
    # show方法，展示基本属性
    def show(self):
        print(f'该产品是{self.brand}品牌的{self.model}型号手机，颜色是{self.color},价格为{self.price}')

    # 开机方法
    def open(self):
        self.ispower_on = True
        print(f'{self.brand}{self.model}已经开机了')

    # 关机方法
    def close(self):
        self.ispower_on = False
        print(f'{self.brand}{self.model}关机了')

    def call(self, number):
        self.open()
        if self.ispower_on:
            print(f'正在使用{self.model}手机打给{number}')
        else:
            print('手机关机了,无法打电话')


iphone = Phone(brand='苹果', color='黑色', model='17pro max', price=8999)
# iphone.show()
# iphone.open()
# iphone.call(19836073866)
# iphone.close()

print(iphone)
del iphone
print(iphone)