import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('>>>:').strip()

    # 不需要判断是不是空，因为还需要发服务端的地址，所以肯定不为空
    # 需要明确指出发给谁以及要发送的数据
    client.sendto(msg.encode('utf-8'), ("127.0.0.1", 8080))
    client.sendto(msg.encode('utf-8'), ("127.0.0.1", 8080))

    # 接收数据
    data1, server_addr = client.recvfrom(1024)
    data2, server_addr = client.recvfrom(1024)
    print(data1)
    print(data2)

client.close()
