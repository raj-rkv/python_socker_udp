import socket
s=socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
serverip="<server_ip>"
port=1234
s.sendto("Hello".encode(),(serverip,port))