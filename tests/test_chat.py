import socket
from emoji import demojize


server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'gaopow'
token = 'oauth:1ib95c0i2z5pst24h7gqiv1041bwe9'
channel = '#xqcow'

sock = socket.socket()

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')
print(resp)

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:
        message = demojize(resp)
        if 'Pog' in message:
            print(message)
 