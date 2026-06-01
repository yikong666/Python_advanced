'''
1.导包
2.创建字符串
3.指定匹配规则
4.匹配
5.查看结果

'''

# 1.导包
import re

# 2.创建字符串
text = '<h1>python</h1><h1>AI</h1><h>大模型</h1>'

# 3.指定匹配规则
tanlan = r'<h1>(.*)</h1>'
feitanlan = r'<h1>(.*?)</h1>'

result1 = re.search(pattern=tanlan, string=text)
result2 = re.search(pattern=feitanlan, string=text)
print(result1.group())
print(result2.group())
