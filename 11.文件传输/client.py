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
    data_size = header_dict["filesize"]
    print(header_dict["filename"])
    print(header_dict["md5"])

    # 接收文件
    with open(filename,'wb') as f:
        recv_size = 0
        while recv_size < data_size:
            line = client.recv(1024)
            f.write(line)
            recv_size += len(line)

client.close()
