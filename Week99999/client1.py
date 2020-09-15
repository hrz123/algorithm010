# client1.py


# s = socket(AF_INET, SOCK_DGRAM)
# s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 8080))
# while True:
#     msg = input('input-1: ')
#     s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
#     data, addr = s.recvfrom(1024)
#     print(data.decode('utf-8'))

# 以下为自我练习
# from socket import *
#
# s = socket(AF_INET, SOCK_DGRAM)
# s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 8080))
# while True:
#     msg = input('input-1: ')
#     s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
#     data, addr = s.recvfrom(1024)
#     print(data.decode('utf-8'))

from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 8080))
while True:
    msg = input('input: ')
    s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
