"""
需求：创建一个基于socket的网络编程客户端端，可以收发消息


服务器开发流程
1.导包，创建socket对象
2.connect(),连接服务器
3.send()发消息，注意编码encode
4.recv()接收并打印，注意解码decode
5.close()，关闭连接，释放资源
"""

# 1.导包
import socket

if __name__ == '__main__':
    # 创建socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.connect(),连接服务器
    # sock.connect(("192.168.36.178", 10086))
    sock.connect(("192.168.36.247", 10084))
    # 3.send()发消息，注意编码encode
    sock.send("今天天机不错".encode("utf-8"))
    # 4.recv()接收并打印，注意解码decode
    result = sock.recv(1024).decode("utf-8")
    print("收到的信息为：", result)
    # 5.close()，关闭连接，释放资源
    sock.close()
