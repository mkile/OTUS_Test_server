import socket
import re

sock = socket.socket(family=socket.AF_INET,
                     type=socket.SOCK_STREAM,
                     proto=0)
sock.bind(('127.0.0.1', 8090))
sock.listen(1)
conn, addr = sock.accept()

print(conn, addr)
data = conn.recv(1024)
print('Recieved', data)

sock.close()
