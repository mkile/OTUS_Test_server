import socket
from http import HTTPStatus
import re

"""
Simple echo server
"""

PROTOCOL = 'HTTP/1.1'
sock = socket.socket(family=socket.AF_INET,
                     type=socket.SOCK_STREAM,
                     proto=0)
sock.bind(('127.0.0.1', 8090))
sock.settimeout(2.0)
sock.listen(1)
respond_codes = list(HTTPStatus)
print('Server started.')
try:
    while True:
        conn = None
        while conn is None:
            try:
                conn, addr = sock.accept()
            except socket.timeout as Err:
                print('.', end='')
        print(conn, addr)
        data = conn.recv(1024)
        data = data.decode('utf-8')
        print('Received data:', data)
        code = re.findall(r'(?:\/\?status=)(\d{3})', data)
        if len(code) > 0:
            code = int(''.join(code))
        print('Received code:', code)
        status = 0
        for list_code in respond_codes:
            if code == list_code.value:
                status = str(list_code.value)
                status_code = list_code.phrase
        if status == 0:
            status = str(HTTPStatus.OK.value)
            status_code = HTTPStatus.OK.phrase
        header = f'{PROTOCOL} {status} {status_code}'

        method = re.findall(r'^[A-Z]+', data)

        response_text = f"""Request Method:{str(method)} Request Source:{addr} Response status:{status} """

        print('Sending:', header)
        conn.send(header.encode('utf-8'))
        conn.send(b'Content-Type: text/html\n')
        conn.send(b'\n')
        print('Sending description:', response_text)
        conn.send(response_text.encode('utf-8'))
        if "%close%" in data:
            conn.send(b'\nServer stopped.')
            raise SystemExit
except (KeyboardInterrupt, SystemExit) as Err:
    sock.close()
    if Err == KeyboardInterrupt:
        print('Keyboard interrupt.')
    else:
        print('Server stopped by remote command.')
