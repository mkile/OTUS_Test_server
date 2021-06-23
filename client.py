import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 8090))
data = input('Введите данные для отправки:')
data = sock.send(data.encode('utf-8'))
data = sock.recv(1024)
print('Recieved:', data.decode('utf-8'))

sock.close()