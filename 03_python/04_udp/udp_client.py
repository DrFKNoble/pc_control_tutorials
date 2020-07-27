#%%
import socket

HOST = "127.0.0.1"
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    
    s.settimeout(2)

    s.sendto('Hello World!'.encode(), (HOST, PORT))

    data, addr = s.recvfrom(12)

    print('Received', data.decode())
    
    s.close()


#%%
