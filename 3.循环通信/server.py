import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
server.listen(5)
print("start...")
conn, client_addr = server.accept()

# 通信循环
while True:
    data = conn.recv(1024)
    print("client data", data)
    conn.send(data.upper())

conn.close()
server.close()
