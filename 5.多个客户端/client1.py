import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(("127.0.0.1", 8080))

while True:
    msg = input(">>>").strip()
    if not msg:
        continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print("receive data:", data.decode('utf-8'))

client.close()
