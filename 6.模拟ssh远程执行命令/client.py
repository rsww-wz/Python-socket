"""
由于服务端是启动了一个终端
退出的时候最好把这个终端闭关了以免占用系统资源
linux用户：pkill -9 Python
Windows用户：taskkill Python
"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

while True:
    # 发命令
    cmd = input(">>>").strip()
    if not cmd:continue
    client.send(cmd.encode("utf-8"))

    # 拿到命令结果
    data = client.recv(1024)
    print(data.decode('GBK'))

client.close()
