import socket, subprocess, struct, json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
server.listen(5)
print("start...")

while True:
    conn, client_addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
            print("client data", cmd.decode('utf-8'))

            # 获取指令结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stdout.read()

            # 报头
            header = {
                "fileName": "a.txt",
                "md5": "xxxdxxx",
                "total_size": len(stdout) + len(stderr),
            }

            # 处理报头
            header_json = json.dumps(header)
            header_bytes = header_json.encode('utf-8')
            header_size = struct.pack('i', len(header_bytes))

            conn.send(header_size)
            conn.send(header_bytes)
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()
server.close()