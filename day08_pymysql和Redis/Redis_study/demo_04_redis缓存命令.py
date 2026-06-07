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
import time

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
    # setex命令，把一个值保存到Redis，并设置缓存时间，以秒为单位
    r.setex("Dify", 1, "AI编程工作流")
    # r.set("Dify","AI编程工作流")
    time.sleep(2)
    # get获取
    value = r.get("Dify")
    print("获取的内容是：", value)
    # 获取剩余时间
    # -2 代表已经超过缓存时间，数据消失了，获取不到了
    # -1 代表没有设置缓存时间，只要没断电一直有
    # 10 代表缓存还剩余10秒
    print("剩余时间为：", r.ttl("Dify"))

finally:
    # 4.关闭连接，结束
    r.close()
