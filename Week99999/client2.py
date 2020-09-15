# client2.py


# s = socket(AF_INET, SOCK_DGRAM)
# s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 8080))
# while True:
#     data, addr = s.recvfrom(1024)
#     print(data.decode('utf-8'))
#     msg = input('input-2: ')
#     s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))

# 以下为自我练习
# from socket import *
#
# s = socket(AF_INET, SOCK_DGRAM)
# s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 8080))
# while True:
#     data, addr = s.recvfrom(1024)
#     print(data.decode('utf-8'))
#     msg = input('input-2: ')
#     s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 8080))
while True:
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    msg = input('input: ')
    s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
