"""
需求：创建一个可以上传文件的客户端

步骤：
1.创建一个socket对象
2.连接服务器，传入服务器的ip和port
3.关联源数据文件，读取内容，发给客户端
4.释放资源
"""
# 1.创建一个socket对象
import socket
sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接服务器，传入服务器的ip和port
sock_obj.connect(("192.168.36.178",10010))

#3.关联源数据文件，读取内容，发给客户端
with open(r"data/data.txt", "rb") as src_file:
    # 5.2 需要一个循环
    while True:
        # 5.3接受客户端上传的文件数
        data = src_file.read(8192)
        # 5.4判断是否为空，如果为空，之后就要结束
        if len(data) == 0:
            break
        # 5.5 把读取来的数据，写入文件中
        sock_obj.send(data)

# 4. 重点！！！告诉服务器"我的数据发完了，你可以回复了"
#    没有这行，服务器不知道客户端发完了，会一直等着收数据
#    客户端等回执，服务器等数据，两个人都等，就卡死了
sock_obj.shutdown(socket.SHUT_WR)  # SHUT_WR = 关闭写通道

#5.解说服务器回执
reply = sock_obj.recv(8192).decode("utf-8")
print(f"客户端收到：\n{reply}")

#6. 关闭连接
sock_obj.close()

