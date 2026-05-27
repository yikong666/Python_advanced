'''
单继承
'''
class GameRole():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self):
        print(f'{self.name}正在移动')

    def show_info(self):
        print(f'[基本信息]名称:{self.name},血量为:{self.hp}')

class SheShou(GameRole):
    def __init__(self, name, hp, lan):
        super().__init__(name, hp)
        self.lan = lan

    def fashe(self):
        print(f'{self.name}射出箭矢')
    
    def move(self):
        print(f'{self.name}正在移动,并释放了法师专属闪现')
    
class FaShi(GameRole):
    def huoyan(self):
        print(f'{self.name}放出火焰')
    
    def show_info(self):
        print(f'[基本信息:最贵的vvvip]名称:{self.name},血量为:{self.hp}')

    
li_yuan_fang = SheShou('李元芳', 100, 500)
li_yuan_fang.move()
li_yuan_fang.show_info()
fairman = FaShi('火男', 120)
fairman.move()
fairman.show_info()
