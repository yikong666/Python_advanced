# 要求：
#
# 1. 提取手机号。
# 2. 删除页码。
# 3. 删除 `【内部资料】`。
# 4. 删除页脚。
# 5. 把连续多个空行压缩为一个换行。

# 1.导包
import re

raw = """
第 1 页
【内部资料】课程答疑记录

学生手机号：13800138000
问题：re.match 和 re.search 有什么区别？


页脚：仅供学习
"""

# 1.提取手机号
phones = re.findall(r'\d{11}', raw)

# 2.删除页码
cleaned = re.sub(r'第\s*\d+\s*页', '', raw)

# 3.删除【内部资料】这类标记。
cleaned = re.sub(r'【.*?】', '', cleaned)

# 4.删除页脚
cleaned = re.sub(r'页脚：.*', '', cleaned)

# 5.压缩重复空行
cleaned = re.sub(r'\n{2,}', '\n', cleaned)

print(phones)

print(cleaned)
