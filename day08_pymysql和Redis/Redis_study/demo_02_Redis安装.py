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

finally:
    # 4.关闭连接
    r.close()
