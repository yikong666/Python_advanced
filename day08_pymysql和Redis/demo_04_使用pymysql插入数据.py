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

# 4.插入数据
try:
    # 4.1.编写sql语句
    sql = "insert into ai_tools values (5, 'Coze', '搭建工作流,但是比dify更简单,网页运行', 1)"
    # 4.2.执行sql语句,execute
    row_count = cursor.execute(sql)
    # 4.3.为保证语句只有一条命令被执行
    if row_count != 1:
        print(f'期望增加一行,但实际运行了{row_count}行')
        conn.rollback()
    # 提交事务
    conn.commit()
# 如果出问题继续回滚
except Exception as e:
    print(e)
    conn.rollback()

# try后除了可以接except,还可以接finally,不管有没有运行成功,都执行
finally:
    # 5.关闭游标
    cursor.close()

    # 6.关闭连接
    conn.close()


