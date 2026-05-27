# 定义 `Task` 类，要求：
class Task(object):
    # 1. 类属性 `total_count`，统计创建了多少个任务对象。
    total_count = 0

    # 2. 实例属性 `title`，保存任务标题。
    def __init__(self, title):
        self.tital = title

    # 3. 成员方法 `finish()`，输出“某任务已完成”。
    def finish(self):
        print(f'{self.tital}任务已完成')

    # 4. 类方法 `show_total_count()`，输出任务总数。
    @classmethod
    def show_total_count(cls):
        cls.total_count += 1
        print(f'任务总数为:{cls.total_count}')

    # 5. 静态方法 `show_rule()`，输出任务规则说明。
    @staticmethod
    def show_rule():
        print("任务规则说明:")
# 6. 创建多个对象并测试三种方法。
task1 = Task('买菜')
task1.finish()
task1.show_total_count()
task2 = Task('洗菜')
task2.finish()
task2.show_total_count()
task3 = Task('炒菜')
task3.finish()
task3.show_total_count()
