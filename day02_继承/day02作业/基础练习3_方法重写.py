# 定义父类 `AiTool`，要求：
class AiTool(object):
    # 1. 属性：`name`、`status`。
    def __init__(self, name, status):
        self.name = name
        self.status = status

    # 2. 方法：`enable()`，把状态改为 `"启用"`；`show_info()`，输出工具信息。
    def enable(self):
        self.status = '启用'

    def show_info(self):
        print(f'工具名称为:{self.name},状态为{self.status}')
    # 3. 定义子类 `DifyTool` 继承 `AiTool`。


class DifyTool(AiTool):
    # 4. `DifyTool` 新增方法 `run_workflow()`，输出“正在运行 Dify 工作流”。
    def run_workflow(self):
        print('正在运行Dify工作流')

    # 重写show_info
    def show_info(self):
        print(f'这是DifyTool重写的show,工具名称是:{self.name},状态为{self.status}')


# 5. 创建对象并测试父类方法和子类方法。
aitool = AiTool('DeepSeek', '停用')
aitool.enable()
aitool.show_info()

difytool = DifyTool('Qwen', '停用')
difytool.enable()
difytool.show_info()

print('-' * 30)
new_difytool = DifyTool('豆包', '停用')
new_difytool.show_info()