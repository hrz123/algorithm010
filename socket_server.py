# socket_server.py

# import socket
#
# # 明确配置变量
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
# # 创建一个TCP套接字
# ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 套接字类型AF_INET，socket.SOCK_STREAM, tcp协议，基于流式的协议
# ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# # 对socket的配置重用ip和端口号
# # 绑定端口号
# ser.bind(ip_port)  # 写哪个ip就要运行在哪台机器上
# # 设置半连接池
# ser.listen(back_log)  # 最多可以连接多少个客户端
# while True:
#     # 阻塞等待，创建连接
#     con, address = ser.accept()  # 在这个位置进行等待，监听端口号
#     while True:
#         try:
#             # 接受套接字的大小，怎么发就怎么收
#             msg = con.recv(buffer_size)
#             if msg.decode('utf-8') == '1':
#                 # 断开连接
#                 con.close()
#             print('服务器收到消息', msg.decode('utf-8'))
#         except Exception as e:
#             break
#     break
# # 关闭服务器
# ser.close()


# 以下为自我练习
# import socket
#
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
# # 创建一个TCP套接字
# ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 套接字类型AF_INET，基于网络类型的，SOCK_STREAM，基于流式的协议
# ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ser.bind(ip_port)  # 写哪个ip就要运行在哪台机器上
# ser.listen(back_log)  # 设定最多可以连接多少个客户端
# while True:
#     # 阻塞式等待，创建连接
#     con, address = ser.accept()
#     print(con)
#     # print(address)  # ('127.0.0.1', 51436)
#     while True:
#         try:
#             # 设定接收套接字的大小
#             msg = con.recv(1024)
#             if msg.decode('utf-8') == '1':
#                 # 如果我们接收到1，就断开连接
#                 con.close()
#                 print("服务端接收到的消息是", msg.decode('utf-8'))
#         except:
#             con.close()
#             break
#     break
# ser.close()


# import socket
#
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
# ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ser.bind(ip_port)
# ser.listen(back_log)
# while True:
#     con, addr = ser.accept()
#     while True:
#         try:
#             msg = con.recv(buffer_size)
#             print("服务端接收到的消息是", msg.decode('utf-8'))
#             if msg.decode('utf-8') == 'q':
#                 break
#         except Exception as e:
#             break
#     con.close()
#     break
# ser.close()
# import socket
#
# ip_port = ('127.0.0.1', 8080)
# backlog = 5
# buffer_size = 1024
# ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ser.bind(ip_port)
# ser.listen(backlog)
# while True:
#     con, addr = ser.accept()
#     while True:
#         try:
#             msg = con.recv(buffer_size)
#             print("服务端收到的消息是", msg.decode('utf-8'))
#             con.send("hello".encode('utf-8'))
#             if msg.decode('utf-8') == 'q':
#                 break
#         except:
#             break
#     con.close()
#     break
# ser.close()
#
# import socket
#
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
#
# ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ser.bind(ip_port)
# ser.listen(back_log)
# while True:
#     con, addr = ser.accept()
#     while True:
#         try:
#             msg = con.recv(buffer_size)
#             print("服务端接收到的数据是", msg.decode('utf-8'))
#             con.send('hello'.encode('utf-8'))
#             if msg.decode('utf-8') == 'q':
#                 break
#         except:
#             break
#     con.close()
#     break
# ser.close()
# from socket import *
#
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# ser = socket(AF_INET, SOCK_STREAM)
# ser.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# ser.bind(ip_port)
# ser.listen(back_log)
# while True:
#     con, addr = ser.accept()
#     while True:
#         msg = con.recv(1024)
#         print("服务端收到的数据是", msg.decode('utf-8'))
#         con.send('hello'.encode('utf-8'))
#         if msg.decode('utf-8') == 'q':
#             break
#     con.close()
#     break
# ser.close()
# from socket import *
#
# ip_port = ('127.0.0.1', 8080)
# backlog = 5
# buffer_size = 1024
# ser = socket(AF_INET, SOCK_STREAM)
# ser.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# ser.bind(ip_port)
# ser.listen(backlog)
# while True:
#     con, addr = ser.accept()
#     while True:
#         msg = con.recv(buffer_size)
#         print("服务端接收到的消息是", msg.decode('utf-8'))
#         con.send('hello'.encode('utf-8'))
#         if msg.decode('utf-8') == 'q':
#             break
#     con.close()
#     break
# ser.close()
# from socket import *
#
# ip_port = ('127.0.0.1', 8080)
# backlog = 5
# buffer_size = 1024
# ser = socket(AF_INET, SOCK_STREAM)
# ser.bind(ip_port)
# ser.listen(backlog)
#
# while True:
#     con, addr = ser.accept()
#     while True:
#         msg = con.recv(buffer_size)
#         print("server get msg: ", msg.decode('utf-8'))
#         con.send('hello'.encode('utf-8'))
#         if msg.decode('utf-8') == 'q':
#             break
#     con.close()
#     break
# ser.close()
# from socket import *
#
# ip_port = ('127.0.0.1', 8080)
# backlog = 5
# buffer_size = 1024
# ser = socket(AF_INET, SOCK_STREAM)
# ser.bind(ip_port)
# ser.listen(backlog)
# while True:
#     con, addr = ser.accept()
#     while True:
#         msg = con.recv(buffer_size)
#         print("server get msg ", msg.decode('utf-8'))
#         con.send('hello'.encode('utf-8'))
#         if msg.decode('utf-8') == 'q':
#             break
#     con.close()
#     break
# ser.close()
from socket import *

ip_port = ('127.0.0.1', 8080)
backlog = 5
buffer_size = 1024
ser = socket(AF_INET, SOCK_STREAM)
ser.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ser.bind(ip_port)
ser.listen(backlog)
while True:
    con, addr = ser.accept()
    while True:
        msg = con.recv(buffer_size)
        print("server recv msg: ", msg.decode('utf-8'))
        con.send("hello".encode('utf-8'))
        if msg.decode('utf-8') == 'q':
            break
    con.close()
    break
ser.close()


def main():
    pass


if __name__ == '__main__':
    main()
