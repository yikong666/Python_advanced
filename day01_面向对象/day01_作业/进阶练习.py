### 综合案例 1：学生成绩管理

# 定义 `ScoreStudent` 类，要求：
#
# 1. 属性：`name`、私有属性 `__score`。
# 2. 分数必须在 `0-100` 之间。
# 3. `set_score(score)`：修改分数，非法分数不允许修改。
# 4. `get_score()`：返回当前分数。
# 5. `is_pass()`：判断是否及格。
# 6. `__str__()`：打印对象时显示学生姓名、分数、是否及格。
# 7. 创建至少两个学生对象测试。
class ScoreStudent:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    # 修改分数
    def set_score(self, score):

        self.__score = score

    # get方法
    def get_score(self):
        return self.__score

    # 判断是否及格
    def is_pass(self):
        if self.__score >= 60:
            print("分数及格")
        else:
            print('不及格')

    # 打印信息
    def __str__(self):
        return f'学生姓名:{self.name},分数:{self.__score}'


stu1 = ScoreStudent('小明', 65)
print(stu1)
stu2 = ScoreStudent('小栓', 50)

### 综合案例 2：AI 服务套餐账号

# 定义 `AiServicePlan` 类，模拟一个 AI 服务套餐账号，要求：
#
# 1. 属性：`username`、`plan_name`、私有属性 `__remain_tokens`。
# 2. `use_tokens(count)`：使用指定 token 数。
# 3. 如果 token 足够，扣减并提示剩余 token。
# 4. 如果 token 不足，提示“不足以完成本次调用”。
# 5. `upgrade_plan(new_plan, add_tokens)`：升级套餐并增加 token。
# 6. `get_remain_tokens()`：查看剩余 token。
# 7. `__str__()`：返回账号、套餐、剩余 token 信息。
