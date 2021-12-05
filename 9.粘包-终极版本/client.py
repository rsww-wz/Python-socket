import socket,struct,json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

while True:
    # 发命令
    cmd = input(">>>").strip()
    if not cmd: continue
    client.send(cmd.encode("utf-8"))

    # 接收报头长度
    header_length = client.recv(4)

    #解析报头长度
    header_size = struct.unpack('i', header_length)[0]

    # 先接收报头
    header_bytes = client.recv(header_size)

    # 解析报头，获取对真是数据的描述
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    data_size = header_dict["total_size"]
    print(header_dict["fileName"])

    # 再接收真实数据
    data = client.recv(data_size)
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
