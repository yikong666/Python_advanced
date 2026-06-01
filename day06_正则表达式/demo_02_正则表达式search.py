'''
步骤
1 导包
2 匹配
3 获取结果
'''
# 1 导包
import re

heima = '1234黑马程序员毕业工作,都是一匹黑马'  # 匹配成功


# 2 匹配
result = re.search(pattern='黑马', string=heima)

if result:
    print(f'search匹配成功:{result.group()}')
else:
    print('search匹配失败')
