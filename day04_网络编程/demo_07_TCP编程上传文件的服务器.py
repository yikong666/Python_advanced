"""
需求：创建一个可以接受文件的服务器

步骤：
1.创建一个socket对象
2.绑定ip和port以元祖的形式传入
3.设置最大监听数
4.等待，返回两个参数，第一个是连接后新返回的专有的对象，第二个参数是客户端的信息ip和port
5.读取客户端上传的文件


"""

# 1.创建一个socket对象
import socket
sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.绑定ip和port以元祖的形式传入
#获取本机IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"本机IP：{local_ip}")
# 2.bind()绑定ip和port
sock_obj.bind((local_ip,10010))
# 3.设置最大监听数
sock_obj.listen(5)
# 4.等待，返回两个参数，第一个是连接后新返回的专有的对象，第二个参数是客户端的信息ip和port
accept_socket,client_info = sock_obj.accept()
# 5.读取客户端上传的文件
# 5.1 创建一个接受数据的地址，通过文件来解说
with open(r"data/result1.txt", "wb") as dest_file:
    # 5.2 需要一个循环
    while True:
        # 5.3接受客户端上传的文件数
        r_bytes = accept_socket.recv(8192)
        # 5.4判断是否为空，如果为空，之后就要结束
        if len(r_bytes) == 0:
            break
        # 5.5 把读取来的数据，写入文件中
        dest_file.write(r_bytes)

#6.给出回执
accept_socket.send("文件上传成功！".encode("utf-8"))

#7.释放资源
accept_socket.close()
sock_obj.close()

