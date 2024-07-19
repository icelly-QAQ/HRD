import socket

IP = "127.0.0.1"

PORT = 23334

BUFLEN = 512

csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

csocket.connect((IP, PORT))

def i_send(ToSend:str):
    csocket.send(ToSend.encode())