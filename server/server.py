import socket

PORT = 1099

class Server():
    def __init__(self):
        self.peers = {} #{"peerName" : {"address" : ["IP", "PORT"], "files" : []}}
        self.socket = socket.socket()
        self.socket.bind(('', PORT))
        self.socket.listen(5)
        print("Socket is listening on "+str(PORT))
    
    def createPeerConnection(self):
        connection,addr = self.socket.accept()
        print('Got connection from', addr)
        connection.send(('Connected: ' + str(addr) ).encode())
        peerName = connection.recv(1024).decode()
        self.peers[peerName] = {}
        self.peers[peerName]["address"] = addr
        return connection

    def getPeerMessage(self,connection):
        message = connection.recv(1024).decode().split(':')
        if message[0] == 'JOIN':
            self.peers[message[1]]["files"] = message[2]
            connection.send('JOIN_OK' .encode())

    def standby(self):
        while True:
            connection = self.createPeerConnection()
            self.getPeerMessage(connection)
            connection.close()
            end = int(input('Digite 0 para sair:'))
            if end == 0:
                break
    pass

def main():
    server = Server()
    server.standby()
    return

main()