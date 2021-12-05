"""
说明
    本程序不实现并发编程
    但是可以保证有并发编程的条件，服务端能一直对外提供服务，即客户端退出了，服务端也不会退出
    不能实现：如果正在处理通信（处理一个请求），不能接收其他请求，要完成本次处理才能接收新的链接

操作
    先运行服务端，再运行客户端，如何客户端不停止，则会一直占用服务器
    直到客户端退出，才能接收其他客户端的请求

并发思路
    链接循环和通信循环独立运行，互不干扰，能够同时运行
"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
server.listen(5)
print("start...")

# 链接循环
while True:
    conn, client_addr = server.accept()

    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
            print("client data", data)
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()
server.close()
