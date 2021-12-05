import socket

# 创建socket对象
# def __init__(self, family=-1, type=-1, proto=-1, fileno=None)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口
# 端口号范围：0-65535
# 0-1024给操作系统使用
server.bind(("127.0.0.1", 8080))

# 监听端口号
server.listen(5)

# 接收客户端请求，监听请求
# 返回值:是元祖类型，客户端对象，客户端连接连接
print("start...")
# res = server.accept()
conn, client_addr = server.accept()
print(conn)
print(client_addr)

# 收数据
# 参数单位是字节，表示接收大多的数据
data = conn.recv(1024)
print("client data", data)

# 发数据
conn.send(data.upper())

# 关闭连接,关闭通信通道
conn.close()

# 关闭服务器
server.close()

"""
服务端有两种套接字
    server:建立连接
    conn:收发数据
"""
