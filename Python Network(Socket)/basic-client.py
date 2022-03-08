wordlist = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']
text = []
import socket
import random

# serverip = 'localhost'
serverip = '104.248.39.146'
port = 27617

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.connect((serverip,port))

while len(text) != 8000:
    w1 = random.choice(wordlist)
    w2 = random.choice(wordlist)
    w3 = random.choice(wordlist)
    t = '{}-{}-{}'.format(w1,w2,w3)
    if t not in text:
        server.send(t.encode('utf-8'))
        print('Data from Server: ', server.recv(1024).decode('utf-8'))
        text.append(t)
         	
server.close()