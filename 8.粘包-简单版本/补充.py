"""
struct 模块
    作用：将数字转成固定长度bytes类型

    打包：pack()
        参数：格式，数据的范围
            i模式：-2147483648 -- 2147483647  固定长度4
            l模式：                           固定长度8
        数据

    解包：unpack()
        返回值：元祖类型

"""
import struct

res = struct.pack('i', 1)
print(res, len(res))

res = struct.pack('i', 128)
print(res, len(res))

res = struct.pack('i', 1024)
print(res, len(res))

res = struct.pack('i', 10240)
print(res, len(res))

res = struct.unpack('i', b'\x80\x00\x00\x00')
print(res)
