import socket

IP = "192.168.0.109"

PORT = 23334

BUFLEN = 512

csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

csocket.connect((IP, PORT))

def i_send(ToSend:str):
    csocket.send(ToSend.encode())