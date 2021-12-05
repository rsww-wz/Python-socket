import socket
import struct
import json
import os
import hashlib

def get(conn,command):
    command = res.decode('utf-8').split(" --")
    filename = command[1]

    # 获取md5值
    obj = hashlib.md5(filename.encode('utf-8'))
    obj.update(filename.encode('utf-8'))
    password = obj.hexdigest()

    # 报头
    header = {
        "filename": filename,
        "md5": password,
        "filesize": os.paht.getsize(filename),
    }

    # 处理报头
    header_json = json.dumps(header)
    header_bytes = header_json.encode('utf-8')
    header_size = struct.pack('i', len(header_bytes))

    # 发送报头大小和报头
    conn.send(header_size)
    conn.send(header_bytes)

    # 发送文件
    with open(filename, 'rb') as f:
        for line in f:
            conn.send(line)


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    print("start...")

    while True:
        conn, client_addr = server.accept()
        while True:
            try:
                res = conn.recv(1024)
                print("client data", res.decode('utf-8'))

                # 解析命令
                # 命令格式：get --filepath
                command = res.decode('utf-8').split(" --")
                if command[0] == "get":
                    get(conn,command)

            except ConnectionResetError:
                break
        conn.close()
    server.close()

if __name__ == "__main__":
    run()
