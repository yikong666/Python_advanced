# 1.导包
import re

text = 'A1D6'

# re.I的作用

result = re.match('[a-z0-9]+', text, re.I)
print(result.group())

# re.S的作用

text1 = '传智\n黑马'
result1 = re.match('.*', text, re.S)
print(result1.group())
