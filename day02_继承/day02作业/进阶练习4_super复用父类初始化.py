# 定义父类 `ModelClient`，要求：
class ModelClient(object):
    # 1. 父类属性：`model_name`、`base_url`。
    def __init__(self, model_name, base_url):
        self.model_name = model_name
        self.base_url = base_url

    # 2. 父类方法：`show_config()`，输出模型名和接口地址。
    def show_config(self):
        print(f'模型名称:{self.model_name},接口地址:{self.base_url}')


# 3. 定义子类 `OpenAIClient`，新增属性 `api_key`。
class OpenAIClient(ModelClient):
    # 4. 子类 `__init__` 中必须使用 `super()` 调用父类初始化。
    def __init__(self, model_name, base_url, api_key):
        super().__init__(model_name, base_url)
        self.api_key = api_key

    # 5. 子类重写 `show_config()`，先调用父类方法，再补充输出 `api_key` 的前 4 位。
    def show_config(self):
        super().show_config()
        print(f'api_key前四位为{self.api_key[:4]}')


chatgpt = OpenAIClient('ChatGPT', 'https:openai.com', '12345678')
chatgpt.show_config()
