#%%
import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32) 
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

    s.bind(('', MCAST_PORT))

    host = socket.gethostbyname(socket.gethostname())
    
    s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
    s.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(host))

    while True:

        data = s.recv(1024)

        if not data:
            break

        print(data.decode())

#%%
