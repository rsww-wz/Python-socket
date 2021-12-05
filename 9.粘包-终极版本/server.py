"""
报头制作的太简单，报头应该是对真是数据的描述信息
可以用字典实现
但是字典每条数据的长度可能不一样，这就造成了报头的长度可能不一样

字典不能用于send发送,send只能发送字节类型
需要先把字典转成json字符串，然后再转成bytes类型
但是这个时候报头的长度不是固定的了

解决方法
    把报头转换成struct类型
    报头的长度就会被打成固定长度

    步骤是：先发送报头长度，再发送报头，最后发送真实数据
"""

import socket, subprocess, struct,json

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

            # 制作报头
            header = {
                "fileName": "a.txt",
                "md5": "xxxdxxx",
                "total_size": len(stdout) + len(stderr),
            }

            # 转成json字符串
            header_json = json.dumps(header)

            # 转成bytes类型
            header_bytes = header_json.encode('utf-8')

            # 把报头长度打成固定长度的bytes类型
            header_size = struct.pack('i',len(header_bytes))

            # 发送报头长度
            conn.send(header_size)

            # 把报头发送给客户端
            conn.send(header_bytes)

            # 发送真是数据,这里如果两者都有内容，会粘包
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()
server.close()
