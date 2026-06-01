# 母题：提取 11 位手机号。
# 变化点：从“纯数字固定长度”变成“字母 P + 4 位数字”。
# 题目：
# text = "订单号: P1001, P2030, X999, P8888"
# 要求：提取所有以 `P` 开头、后面跟 4 位数字的订单号。
# 1.导包
import re

# 2.要处理的文本
text = "订单号: P1001, P2030, X999, P8888"

dingdan = re.findall(pattern=r'P\d{4}', string=text)

print(dingdan)
