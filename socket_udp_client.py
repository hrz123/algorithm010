# socket_udp_client.py

# from socket import *
#
# s = socket(AF_INET, SOCK_DGRAM)
# while True:
#     msg = input('input-1: ')
#     s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
#     data, addr = s.recvfrom(1024)
#     print(data.decode('utf-8'))
# # s.close()

# 以下为自我练习
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# while True:
#     msg = input("please input: ")
#     s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
#     data, addr = s.recvfrom(1024)
#     print(data.decode('utf-8'))
# # s.close()
# import socket
#
# p = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# while True:
#     msg = input('please input: ')
#     p.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
#     data, addr = p.recvfrom(1024)
#     print(data.decode('utf-8'))
#     if msg == 'q':
#         break
# p.close()
# from socket import *
#
# p = socket(AF_INET, SOCK_DGRAM)
# while True:
#     msg = input('please input: ')
#     p.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
#     data, addr = p.recvfrom(1024)
#     print(data.decode('utf-8'), addr)
#     if msg == 'q':
#         break
# p.close()

from socket import *

p = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input('please input: ')
    p.sendto(msg.encode('utf-8'), ("127.0.0.1", 8080))
    data, addr = p.recvfrom(1024)
    print(data.decode('utf-8'))
    if msg == 'q':
        break
p.close()
