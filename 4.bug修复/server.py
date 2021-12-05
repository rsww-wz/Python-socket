import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
server.listen(5)
print("start...")
conn, client_addr = server.accept()

# 通信循环
while True:
    # linux适用
    """
    # 如果客户端连接断掉，在linux服务端会进入死循环
    data = conn.recv(1024)
    
    if not data:
        break
    print("client data", data)
    conn.send(data.upper())
    """

    # windows适用
    # 如果客户端连接断掉，在Windows程序会直接报错
    try:
        data = conn.recv(1024)
        print("client data", data)
        conn.send(data.upper())
    except ConnectionResetError:
        break

conn.close()
server.close()
