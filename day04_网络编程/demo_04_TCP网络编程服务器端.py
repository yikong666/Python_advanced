"""
需求：创建一个基于socket的网络编程服务器端，使用ipv4和tcp协议，负责收发消息


服务器开发流程
1.导包，创建socket对象
2.bind()，绑定ip和port
3.listen(),监听，设置监听数，最大值128
4.accept(),等待接收，阻塞一直等到接收为止，返回1.socket专线2.客户端ip和port
5.recv()接收并打印，注意解码decode
6.send()发消息，注意编码encode
7.close()，关闭连接，释放资源
"""

# 1.导包
import socket

if __name__ == '__main__':
    # 创建socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本机IP
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("本机IP：", local_ip)
    # 2.bind()，绑定ip和port
    sock.bind((local_ip, 10084))
    # sock.bind(("127.0.0.1",10086))
    # 3.listen(),监听，设置监听数，最大值128
    sock.listen(5)
    # 4.accept(),等待接收，阻塞一直等到接收为止，返回1.socket专线2.客户端ip和port
    accpet_socket, client_info = sock.accept()
    print("专属socket连接，专线：", accpet_socket)
    print("客户端信息：", client_info)
    # 5.recv()接收并打印，注意解码decode
    result = accpet_socket.recv(1024).decode("utf-8")
    print(f"收到的信息为：{result}\n")
    # 6.send()发消息，注意编码encode
    accpet_socket.send("接收到客户端请求了，回复：你好客户端".encode("utf-8"))
    # 7.close()，关闭连接，释放资源
    accpet_socket.close()
