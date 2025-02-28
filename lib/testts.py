import socket

IP = "0.0.0.0"

PORT = 23334

BUFLEN = 512

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

while True:
    serversocket.listen(1)

    data, addr = serversocket.accept()

    while True:

        recved = data.recv(BUFLEN)

        if not recved:
            break
            
        info = recved.decode()
        print(f"接收信息：「{info}」发送方：「{addr}」")
