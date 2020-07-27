#%%
import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.settimeout(2)

    s.connect((HOST, PORT))

    s.send('Hello World!'.encode())

    data = s.recv(12)

    print('Received', data.decode())

    s.close()

#%%
