import socket
s = socket.socket()
s.connect(('localhost', 6000))
print(s.getsockname())
print(s.recv(1024).decode())
s.send("acknowledgement received from the server".encode())