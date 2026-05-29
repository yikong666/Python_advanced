'''
创建一个socket对象
第一个参数值ipv4或ipv6
第二个参数值TCP或UDP

步骤
1 导包
2 创建实例化对象
3 填参数
'''
# 1 导包
import socket

# 2 创建实例化对象
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket_obj)