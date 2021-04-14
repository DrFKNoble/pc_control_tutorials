#%%
import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))

    s.listen(1)
   
    conn, addr = s.accept()

    with conn:

        print('Connect by ', addr)

        while True:

            data = conn.recv(12)

            if not data:
                break
                
            print('Received ', data.decode())

            conn.sendall(data)

    s.close()
#%%
