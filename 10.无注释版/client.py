import socket, struct, json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

while True:
    cmd = input(">>>").strip()
    if not cmd: continue
    client.send(cmd.encode("utf-8"))

    # 接收报头长度
    header_length = client.recv(4)
    header_size = struct.unpack('i', header_length)[0]

    # 接收并解析报头
    header_bytes = client.recv(header_size)
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    data_size = header_dict["total_size"]
    print(header_dict["fileName"])

    # 接收指令结果
    data = client.recv(data_size)
    print(data.decode('GBK'))
client.close()
