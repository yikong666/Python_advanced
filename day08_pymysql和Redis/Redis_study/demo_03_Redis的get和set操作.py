# 1.导包
import redis

# 2.创建链接
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True,
    protocol=2
)

try:
    # 3.ping包
    print('Redis是否连接成功:', r.ping())
    # set命令,把一个值保存到Redis
    r.set('day08:redis:intro', 'redis可以用来作缓存')

    value = r.get('day08:redis:intro')
    print('获取的内容是:',value)
finally:
    # 4.关闭连接
    r.close()
