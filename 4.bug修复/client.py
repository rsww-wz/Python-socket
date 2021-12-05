import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

while True:
    msg = input(">>>").strip()
    # 如果msg是空字符串，操作系统不会发送数据
    if not msg:
        continue
    # 底层是和操作系统交互，把数据发送给操作系统，然后用网卡把数据发送出去
    client.send(msg.encode("utf-8"))
    # 底层是和操作系统交互，网卡接收的数据给操作系统，然后程序与操作系统交互
    # 程序完成应用层功能，操作系统完成应用层以下的功能
    data = client.recv(1024)
    print("receive data:", data.decode('utf-8'))

client.close()
