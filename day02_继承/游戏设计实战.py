class Game(object):
    # 定义类属性:存储总积分
    all_score = 0

    def __init__(self, name):
        # 定义成员属性
        self.name = name

    # 定义静态方法
    @staticmethod
    def show_help():
        print('游戏信息须知:每个玩家玩一次积分增加1')

    # 定义类方法:显示历史总积分的方法
    @classmethod
    def show_all_score(cls):
        print(f'当前总计分为:{cls.all_score}分')

    # 定义成员方法:玩家玩游戏
    def start_game(self):
        print(f'{self.name}玩家玩了一局,总积分加1')
        Game.all_score += 1
# 显示帮助信息
Game.show_help()
Game.show_all_score()
xiaoming = Game('小明')

xiaohong = Game('小红')
