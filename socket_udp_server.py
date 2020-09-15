# socket_udp_server.py

# from socket import *
#
# udp_ser = socket(AF_INET, SOCK_DGRAM)  # 数据报式的套接字
# udp_ser.bind(('127.0.0.1', 8080))
#
# while True:
#     data = udp_ser.recvfrom(1024)
#     print(data)  # (b'asd', ('127.0.0.1', 60606))
#     udp_ser.sendto('data'.encode('utf-8'), data[1])

# udp_ser.close()

# 以下为自我练习
# import socket
#
# udp_ser = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp_ser.bind(('127.0.0.1', 8080))
# while True:
#     data, addr = udp_ser.recvfrom(1024)  # recvfrom返回的结果是收到的信息和发送方的ip和端口号
#     print(data, addr)
#     udp_ser.sendto('hello'.encode('utf-8'), addr)
# udp_ser.close()

# import socket
#
# udp_ser = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp_ser.bind(('127.0.0.1', 8080))
# while True:
#     data, addr = udp_ser.recvfrom(1024)
#     print(data, addr)
#     udp_ser.sendto('hello'.encode('utf-8'), addr)
#     if data.decode('utf-8') == 'q':
#         break
# udp_ser.close()
# from socket import *
#
# udp_ser = socket(AF_INET, SOCK_DGRAM)
# udp_ser.bind(('127.0.0.1', 8080))
# while True:
#     data, addr = udp_ser.recvfrom(1024)
#     print(data.decode('utf-8'), addr)
#     udp_ser.sendto('hello'.encode('utf-8'), addr)
#     if data.decode('utf-8') == 'q':
#         break
# udp_ser.close()
from socket import *
udp_ser = socket(AF_INET, SOCK_DGRAM)
udp_ser.bind(('127.0.0.1', 8080))
while True:
    data, addr = udp_ser.recvfrom(1024)
    print(data.decode('utf-8'))
    udp_ser.sendto('hello'.encode('utf-8'), addr)
    if data.decode('utf-8') == 'q':
        break
udp_ser.close()