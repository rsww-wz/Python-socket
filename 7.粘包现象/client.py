import socket,time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

# 时间间隔短，把两次数据一次发送了
client.send("hello".encode('utf-8'))

# 手动延长间隔时间
# time.sleep(1)

client.send("world".encode('utf-8'))
client.close()
