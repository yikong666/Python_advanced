# 设计一个 AI 工具管理中心，要求：
# 1. 定义父类 `BaseTool`，包含工具名 `name`、私有状态 `__enabled`。
class BaseTool(object):
    def __init__(self, name, enabled):
        self.name = name
        self.__enabled = enabled

    # 2. 提供 `enable()`、`disable()`、`is_enabled()` 方法控制和查看状态。
    def enable(self):
        self.__enabled = True
        print(f'{self.name}工具现已开启')

    def disable(self):
        self.__enabled = False
        print(f'{self.name}工具现已停用')

    def is_enabled(self):
        return self.__enabled


# 3. 定义 `DifyTool` 和 `OpenAITool` 继承 `BaseTool`。
class DifyTool(BaseTool):
    # 4. 两个子类都实现自己的 `run()` 方法。
    def run(self):
        print('Dify模型已经运行起来了')


class OpenAITool(BaseTool):
    # 4. 两个子类都实现自己的 `run()` 方法。
    def run(self):
        print('OpenAI模型已经运行起来了')


# 5. 定义统一函数 `run_tool(tool)`：如果工具已启用，就调用 `tool.run()`；否则提示工具未启用。
def run_tool(tool):
    if tool.is_enabled():
        tool.run()
    else:
        print(f'{tool.name}工具未启用')


# 6. 创建两个工具对象，分别测试启用前和启用后的运行效果。

dify = DifyTool('Dify', False)
openai = OpenAITool('ChatGPT', False)
dify.enable()

openai.enable()

for i in (dify, openai):
    run_tool(i)
