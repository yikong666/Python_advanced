# 设计一个课程学习系统，要求：

# 1. 定义 `Course` 类，类属性 `total_learning_minutes` 统计全班累计学习分钟数。
class Course(object):
    total_learning_minutes = 0

    # 2. 实例属性：课程名 `name`、学生名 `student_name`。
    def __init__(self, name, student_name):
        self.name = name
        self.student_name = student_name

    # 3. 成员方法 `learn(minutes)`：某学生学习某课程指定分钟数，并累加到全班总学习时长。
    def learn(self, minutes):
        if minutes <= 0:
            print('学习时间过短')
            return
        else:
            print(f'{self.student_name}学习了{self.name}{minutes}分钟')
            Course.total_learning_minutes += minutes

    # 4. 类方法 `show_total_minutes()`：输出全班总学习分钟数。
    @classmethod
    def show_total_minutes(cls):
        print(f'全班总学习时长:{cls.total_learning_minutes}分钟')

        # 5. 静态方法 `show_rule()`：输出学习规则。

    @staticmethod
    def show_rule():
        print('学习规则:某学生学习某课程指定分钟数，并累加到全班总学习时长')


# 6. 创建至少两个课程对象，测试学习和总时长统计。

math = Course('数学', '小明')
math.show_rule()
math.learn(90)
datebase = Course('数据库', '小红')
datebase.learn(10)
Course.show_total_minutes()
