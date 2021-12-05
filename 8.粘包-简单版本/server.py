import socket, subprocess,struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
server.listen(5)
print("start...")

while True:
    conn, client_addr = server.accept()
    while True:
        try:
            # 收命令
            cmd = conn.recv(1024)
            print("client data", cmd)

            # 执行命令，把命令拿到操作系统执行，并拿到的结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stdout.read()

            # 制作固定长度的报头
            header = struct.pack('i', len(stdout) + len(stderr))

            # 把报头发送给客户端
            conn.send(header)

            # 发送真是数据,这里如果两者都有内容，会粘包
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()
server.close()
