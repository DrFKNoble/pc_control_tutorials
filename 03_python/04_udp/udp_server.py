#%%
import socket

HOST = '127.0.0.1'
PORT = 61556

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind((HOST, PORT))

    while True:
     
        data, addr = s.recvfrom(12)
     
        print('Connect by ', addr)
        print('Received ', data.decode())

        if not data: 
            break

        s.sendto(data, addr)

    s.close()
#%%
