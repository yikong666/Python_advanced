# 定义三个类：
# 1. `DifyRunner`，有 `run()` 方法。
class DifyRunner(object):
    def run(self):
        print('Dify模型正在跑')


# 2. `OpenAIRunner`，有 `run()` 方法。
class OpenAIRunner(object):
    def run(self):
        print('OpenAI模型正在跑')


# 3. `LocalRunner`，有 `run()` 方法。
class LocalRunner(object):
    def run(self):
        print('本地模型正在跑')


# 再定义函数 `start_runner(runner)`，要求：
def start_runner(runner):
    # 1. 函数内部统一调用 `runner.run()`。
    runner.run()


# 2. 分别传入三个不同对象，观察同一个函数表现出不同结果。
dify = DifyRunner()
openai = OpenAIRunner()
local = LocalRunner()
for i in (dify, openai, local):
    start_runner(i)
