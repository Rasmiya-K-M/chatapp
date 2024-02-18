import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)


client,address=s.accept()
while True:
    smessage=input("Server: ")
    client.send(bytes(smessage,"utf-8"))
    cmessage=client.recv(50)
    print("Client: "+ cmessage.decode('utf-8'))