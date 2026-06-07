"""
需求：
使用redis连接数据库，ping通，返回结果

步骤：
1.导包
2.创建连接
3.ping信息
4.关闭连接，结束
"""

# 1.导包
import redis

# 2.创建连接
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True,
    protocol=2  # 版本低的同学加一下
)

try:
    # 3.ping信息
    print("Redis是否连接成功:", r.ping())
    # 自增,首先设置counter计数
    r.set('counter', 0)
    result = r.get('counter')
    print('初始值是:', result)

    # 测试自增incr
    r.incr('counter', 5)
    print(f'自增5后,值为:{r.get('counter')}')

    # 测试自减decr
    r.decr('counter', 6)
    print(f'自减6后,值为:{r.get('counter')}')


finally:
    # 4.关闭连接，结束
    r.close()
