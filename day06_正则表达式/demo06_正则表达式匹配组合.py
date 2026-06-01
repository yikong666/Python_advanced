'''
使用正则表达式,匹配组合的方式,包括
| () \1

1.导包
2.创建字符串
3.创建匹配格式传入表达式
4.查看结果 分析
'''

# 1.导包
import re

# 2.创建字符串
# text = 'heima@sohu.com'
#
# # 3.创建匹配格式传入表达式
# pattern = r'([a-zA-Z0-9_]{4,20})@(163|sina|sohu)\.com'
# result = re.match(pattern=pattern, string=text)
# print(result.group())

email = 'wby3866@163.com'
pattern = r'(.*)@(.*)'
match = re.match(pattern, email)
print(match.group(1))
print(match.group(2))
print(match.group())

# 匹配网页格式
text1 = '<html>标签内容</html>'
pattern1 = r'<([a-zA-Z0-9]+)>.*</\1>'  # 前边有r的时候后边内容无需转义,因为r已经转义了
# pattern2 = '<([a-zA-Z0-9]+)>.*</\\1>'   # 无r的时候后边有\要转义

result = re.match(pattern=pattern1, string=text1)
print(result.group())

# 起别名的方式来匹配组
pattern3 = r'<(?P<lable>[a-zA-Z0-9]+)>.*</(?P=lable)>'
result3 = re.match(pattern=pattern3, string=text1)
print(result.group())
