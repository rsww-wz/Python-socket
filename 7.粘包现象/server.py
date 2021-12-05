import socket, subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
server.listen(5)
print("start...")

conn,addr = server.accept()

# 数据没有收完也会造成粘包现象
res1 = conn.recv(1)
print("first time:",res1)

# 第二次的数据被第一次接收了，造成了粘包现象
res2 = conn.recv(1024)
print("second time:",res2)

conn.close()
server.close()
