'''
步骤
1 导包
2 匹配
3 获取结果
'''
# 1 导包
import re

heima = '黑马程序员毕业工作,都是一匹黑马'
# heima = '12343534534黑马程序员毕业工作,都是一匹黑马'


# 2 匹配
result = re.match(pattern='黑马', string=heima)

if result:
    print(f'match匹配成功：{result.group()}')
else:
    print('match匹配失败')