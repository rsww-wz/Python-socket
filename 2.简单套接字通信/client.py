import socket

# 创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 客户端不需要绑定IP地址和端口，因为他们是可以变的
# 客户端需要做的是发起请求,发起请求需要先建立通道
client.connect(("127.0.0.1", 8080))

# 发数据
# 数据不能直接用字符串格式发送，最终传输的是二进制，所有需要转换编码
client.send("hello".encode("utf-8"))

# 收数据
data = client.recv(1024)
print("recvice data:",data)

# 关闭连接通道
client.close()