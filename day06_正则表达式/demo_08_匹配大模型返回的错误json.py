import re
import json


def clean_llm_json(llm_output):
    """
    专门用于清洗大模型输出的 JSON 字符串。
    应对场景：外层包裹了 ```json ... ```，或者前后带有废话解释。
    """

    # 【核心正则解析】
    # \{  : 匹配左大括号 (因为 { 在正则中有特殊含义，所以需要用 \ 转义)
    # .* : 匹配任意字符，而且是“贪婪模式”（会一直往后找，直到找到最后一个 } 为止）
    # \}  : 匹配右大括号
    pattern = r'\{.*\}'

    # re.DOTALL (或简写 re.S) 是这句代码的灵魂！
    # 默认情况下，正则里的 '.' 是不能匹配换行符的。
    # 但大模型的 JSON 通常都是多行的，加上 re.DOTALL，就能让 '.' 匹配包括换行符在内的所有字符。
    match = re.search(pattern, llm_output, re.DOTALL)

    if match:
        # group(0) 拿到的就是被提取出来的、干干净净的 JSON 字符串
        json_string = match.group(0)

        try:
            # 顺手做个反序列化，验证它到底是不是合法的 JSON，变成 Python 的字典
            data_dict = json.loads(json_string)
            return data_dict
        except json.JSONDecodeError:
            print("❌ 正则提取成功了，但里面的 JSON 语法有错（比如少了个逗号）")
            return None
    else:
        print("❌ 字符串里根本没有大括号，提取失败")
        return None


# ==========================================
# 🏫 课堂测试环节 (设计了三种典型的“翻车”场景)
# ==========================================

print("=== 测试 1：标准的 Markdown 包裹 ===")
test_1 = """
这里是为您生成的 JSON 数据：
```json
{
    "name": "张三",
    "age": 28,
    "skills": ["Python", "Prompt Engineering"]
}
希望对您有帮助！
"""

result1 = clean_llm_json(test_1)
print("提取结果:", result1)
print("类型:", type(result1))

print("\n=== 测试 2：前后都有大段废话的纯文本 ===")
test_2 = """
好的，根据您的要求，我分析了用户的意图。
{
"intent": "query_database",
"table": "user_info",
"confidence": 0.95
}
这是最终的判断结果，您可以将这个 JSON 传给下一个 Agent 节点。
"""
result2 = clean_llm_json(test_2)
print("提取结果:", result2)

print("\n=== 测试 3：单行 JSON (也没有问题) ===")
test_3 = '返回结果为: {"status": "success", "code": 200}'
result3 = clean_llm_json(test_3)
print("提取结果:", result3)


# result = {"label":"非噪音"}