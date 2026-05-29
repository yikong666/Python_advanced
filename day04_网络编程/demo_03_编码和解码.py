'''
需求: Tcp服务面向字节流,要进行转换
编码 字符串变成字节.二进制数字
解码 把2进制数字变成看的懂的字符串

步骤
1 编码:将字符串转为面相字节流二进制字节
str.encode(utf-8)
2 解码 把二进制字符串转换为文字字符串
bytes.decode(utf-8)
'''

# 1 编码:将字符串转为面相字节流二进制字节
s1 = '黑马123wang!@#$'

print(s1.encode(encoding='utf-8'))

s2 = s1.encode(encoding='utf-8')
print(s2.decode(encoding='utf-8'))

print('-'*30)
# 换为gbk编码
s3 = s1.encode(encoding='gbk')
print(s3)
s4 = s3.decode(encoding='gbk')
print(s4)