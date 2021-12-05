"""
指令命令，拿到结果
    os库
        调用OS库，用os.system把命令交给操作系统执行
        它的效果是直接在终端打印获取到的结果
        但是os.system的返回值是不是获取到的命令，而是0和非零
        0表示命令执行成功，非零表示命令执行失败
        所以用os库不能完成

    subprocess
        subprocess.Popen()
        参数
            命令字符串
            shell=TRUE，表示操作系统启动一个终端，把命令放到终端中去执行
            stdout=subprocess.PIPE
            stderr=subprocess.PIPE

        返回值：返回一个对象
            对象里面有标准输入，标准输出，标准错误输出
            返回都是bytes格式
            在linux用utf-8解码
            在Windows用GBK解码


        但是还是拿不到命令执行的结果，但是有解决的办法
        在终端中有一个重定向的指令，可以把结果重定向到某个指定位置，然后读取它就能获得结果

        函数也提供了一个stdout，stderr参数，能实现类似的功能
        PIPE表面上是一个属性，实际上是一个装饰器

"""

import os,subprocess

# os.system('ipconfig')
obj = subprocess.Popen("ipconfig", shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

# 读取标准输出,返回的是bytes格式
print(obj.stdout.read().decode('GBK'))

# 读取错误输出
print(obj.stderr.read().decode('GBK'))