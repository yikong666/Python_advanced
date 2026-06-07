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

# 4.查询
try:
    # 4.1.编写sql语句
    sql = 'select * from ai_tools'
    # 4.2.执行sql语句,execute
    row_count = cursor.execute(sql)
    # 4.3.获取查询结果fetchall或fetchone
    rows = cursor.fetchall()
    # 4.4 打印结果
    print(f'当前一共查询到{row_count}行数据')
    for id, name, sence, status in rows:
        status_text = '已启用' if status == 1 else '未启用'
        print(f'编号:{id},工具名:{name},场景:{sence},状态:{status_text}')

# try后除了可以接except,还可以接finally,不管有没有运行成功,都执行
finally:
    # 5.关闭游标
    cursor.close()

    # 6.关闭连接
    conn.close()


