"""
UDP：数据报协程
对于UDP，必须是一个sendto对应于recvfrom
所以不存在粘包现象
"""

import socket

# 新建服务端对象
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定IP地址端口
server.bind(("127.0.0.1", 8080))
print("start...")

# 只有链接循环，没有通信循环，因为UDP通信不需要建立通道，没有三次握手
while True:
    # 收消息
    # 第二个返回值是客户端的地址，如果要发送消息的话，需要记录发过来客户端地址
    data1, client_addr = server.recvfrom(1024)
    data2, client_addr = server.recvfrom(1024)
    print(data1)
    print(data2)

    # 发消息
    server.sendto(data1.upper(), client_addr)
    server.sendto(data2.lower(), client_addr)

server.close()
