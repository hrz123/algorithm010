# socket_client.py

# import socket
#
# p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while 1:
#     msg = input('please input: ')
#     # 防止输入空消息
#     if not msg:
#         continue
#     p.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码
#     if msg == '1':
#         break
# p.close()


# 以下为自我练习
# import socket
#
# p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input("please input: ")
#     if not msg:
#         continue
#     p.send(msg.encode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
# import socket
#
# p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input('please input: ')
#     p.send(msg.encode('utf-8'))
#     data = p.recv(1024)
#     print(data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
# import socket
#
# p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input('please input: ')
#     p.send(msg.encode('utf-8'))
#     data = p.recv(1024)
#     print(data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
# from socket import *
#
# p = socket(AF_INET, SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input("please input: ")
#     p.send(msg.encode('utf-8'))
#     data = p.recv(1024)
#     print("客户端接收到的数据是", data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()

# from socket import *
#
# p = socket(AF_INET, SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input('please input: ')
#     p.send(msg.encode('utf-8'))
#     data = p.recv(1024)
#     print(data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
# from socket import *
#
# p = socket(AF_INET, SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input('please input: ')
#     p.send(msg.encode('utf-8'))
#     data = p.recv(1024)
#     print('client receive', data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
# from socket import *
#
# p = socket(AF_INET, SOCK_STREAM)
# p.connect(('127.0.0.1', 8080))
# while True:
#     msg = input('please input: ')
#     p.send(msg.encode('utf-8'))
#     data = p.recv(1024)
#     print("client get msg: ", data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
from socket import *

p = socket(AF_INET, SOCK_STREAM)
p.connect(('127.0.0.1', 8080))
while True:
    msg = input("please input: ")
    p.send(msg.encode('utf-8'))
    data = p.recv(1024)
    print("client get msg: ", data.decode('utf-8'))
    if msg == 'q':
        break
p.close()


def main():
    pass


if __name__ == '__main__':
    main()
