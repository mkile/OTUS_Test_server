import socket
from http import HTTPStatus
import re

sock = socket.socket(family=socket.AF_INET,
                     type=socket.SOCK_STREAM,
                     proto=0)
sock.bind(('127.0.0.1', 8090))
sock.listen(1)
while True:
    conn, addr = sock.accept()

    print(conn, addr)
    data = conn.recv(1024)
    print('Recieved', data)
    protocol = 'HTTP/1.1'
    status = str(HTTPStatus.OK.value)
    status_code = HTTPStatus.OK.phrase
    message = f'{protocol} {status} {status_code}'
    conn.send(message.encode('utf-8'))

sock.close()
