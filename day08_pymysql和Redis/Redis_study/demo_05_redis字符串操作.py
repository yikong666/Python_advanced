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
    # set命令，把一个值保存到Redis
    r.set("name", "张三")
    r.set("age", "25")

    # 获取get
    name = r.get("name")
    age = r.get("age")
    print(f"姓名：{name},年龄：{age}")

    # 设置多个值
    # mset要设置字典格式
    r.mset({"city": "北京", "job": "工程师"})
    # 获取多个值
    # mget要是列表格式，里面是存入的key
    values = r.mget(["name", "age", "city", "job"])
    print("多个值：", values)

finally:
    # 4.关闭连接，结束
    r.close()
