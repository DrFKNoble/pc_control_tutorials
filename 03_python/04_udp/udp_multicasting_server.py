#%%
import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 50007
MULTICAST_TTL = 1

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:

    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
    
    s.sendto("Hello World!".encode(), (MCAST_GRP, MCAST_PORT))