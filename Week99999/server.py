# server.py


# udp_ser = socket(AF_INET, SOCK_DGRAM)  # 数据报式的套接字
# udp_ser.bind(('127.0.0.1', 8080))
# data_1, addr_1 = udp_ser.recvfrom(1204)
# data_2, addr_2 = udp_ser.recvfrom(1204)
# while True:
#     # udp_ser.sendto('你好'.encode('utf-8'))
#     data1 = udp_ser.recvfrom(1204)
#     udp_ser.sendto(data1[0], addr_2)
#     data2 = udp_ser.recvfrom(1204)
#     # udp_ser.sendto(data,)
#     udp_ser.sendto(data2[0], addr_1)

# 以下为自我练习
# from socket import *
#
# udp_ser = socket(AF_INET, SOCK_DGRAM)
# udp_ser.bind(('127.0.0.1', 8080))
# data_1, addr_1 = udp_ser.recvfrom(1024)
# data_2, addr_2 = udp_ser.recvfrom(1024)
# while True:
#     data1 = udp_ser.recvfrom(1024)
#     udp_ser.sendto(data1[0], addr_2)
#     data2 = udp_ser.recvfrom(1024)
#     udp_ser.sendto(data2[0], addr_1)
from socket import *

udp_ser = socket(AF_INET, SOCK_DGRAM)
udp_ser.bind(('127.0.0.1', 8080))
data1, addr1 = udp_ser.recvfrom(1024)
data2, addr2 = udp_ser.recvfrom(1024)
while True:
    data1 = udp_ser.recvfrom(1024)[0]
    udp_ser.sendto(data1, addr2)
    data2 = udp_ser.recvfrom(1024)[0]
    udp_ser.sendto(data2, addr1)
