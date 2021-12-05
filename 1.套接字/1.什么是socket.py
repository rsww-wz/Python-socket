"""
基于网络编程 = 客户端 + 服务端
客户端和服务端都是部署在应用层
基于网络通信就需要实现：物理层，数据链路层，网络层，传输层
而socket就是在应用层和传输层之间的抽象层，封装好了传输层以下的功能，只暴露了所需要的接口，从而大大简化了学习成本

传输层分为TCP和UDP两种
    TCP是基于流式编程，需要先建立好通道，提供可靠服务
    UDP是基于报文编程，不提供可靠服务

    而socket也有这两种形式

Socket
    是应用层与 TCP/IP协议族通信的中间软件抽象层，它是一组接口
    在设计模式中， Socket其实就是一个门面模式，它把复杂的 TCP/IP协议族隐藏在Sockett接口后面
    对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议
    所以，我们无需深入理解tcp/udp协议,socket已经为我们封装好了
    我们只需要循 sockets的规定去编程，写出的程序自然就是遵循tcp/udp标准的

socket
    socket也叫套接字
    socket = ip + 端口
    因为物理层，数据链路层和网络层就是解决IP问题
    而传输层就是解决端口问题
"""