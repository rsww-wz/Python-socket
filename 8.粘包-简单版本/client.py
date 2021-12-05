import socket,struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

while True:
    # 发命令
    cmd = input(">>>").strip()
    if not cmd: continue
    client.send(cmd.encode("utf-8"))

    # 先接收报头
    header = client.recv(4)

    # 解析报头，获取对真是数据的描述
    total_size = struct.unpack('i', header)[0]

    # 再接收真实数据
    data = client.recv(total_size)
    print(data.decode('GBK'))
    """
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = client.recv(50)
        recv_data += res
        recv_size += len(res)

    print(recv_data.decode('GBK'))
    """
client.close()
