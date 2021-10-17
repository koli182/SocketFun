import socket

SRV_ADDR = input("Type in your server IP address: ")
SRV_PORT = int(input("Type in your server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Your server has started! Waiting for any connections...")
connection, address = s.accept()
print("Client has successfully connected with an address of:", address)
while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()


