# 1.导包
import pymysql

# 2.创建链接connection
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='ai_work_demo',
    charset='utf8'
)

# 3.创建游标cursor
cursor = conn.cursor()

# 4.打印状态，先不执行
print("数据库连接成功了")

# 5.关闭游标
cursor.close()

# 6.关闭连接
conn.close()
