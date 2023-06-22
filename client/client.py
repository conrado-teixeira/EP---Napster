import socket
import os

IP = '127.0.0.1'
PORT = 1099 

class Peer:
    def __init__(self, ip, port, folderPath):
        self.name = folderPath.split('\\')[-1]
        self.socket = socket.socket()
        self.address = (ip, port)
        self.folder = folderPath
        self.getFilesList()

    # def getPeerFolder(self, folderPath):
    #     folderPath = os.path.dirname(os.path.abspath(__file__))+"/"+folderPath
    #     if not os.path.exists(folderPath):
    #         os.makedirs(folderPath)

    #     return folderPath

    def getFilesList(self):
        self.filesList = os.listdir(self.folder)
        return self.filesList
    
    def createServerConnection(self):
        s = self.socket
        s.connect((IP, PORT))
        message =  s.recv(1024).decode().split(':')
        if message[0] == 'Connected':
            self.address = message[1].strip()
            print(self.address)
            self.socket.send((self.name).encode())

    
    def closeConnection(self):
        self.socket.close()

    def joinRequest(self):
        self.socket.send( ('JOIN:'+self.name+':'+str(self.filesList)).encode())
        print(self.socket.recv(1024).decode())

         
    pass

def main():
    ip, port, folderPath = input('Informe IP, Porta e Pasta do Peer, neesa ordem, separadas por | : ').split('|')
    peer = Peer(ip.strip(), port.strip(), folderPath.strip()) 

    while True:
        cmd = input("Digite a requisição deseja fazer (JOIN ou SEARCH ou DOWNLOAD): ")      
        #join
        if cmd.upper().strip() == 'JOIN':   
            peer.createServerConnection()
            peer.joinRequest()
        elif cmd.upper() == 'SEARCH':
            print('TODO/: SEARCH')
        elif cmd.upper() == 'DOWNLOAD':
            print('TODO/: DOWNLOAD')







    end = input('Aperte ENTER para fechar')
    return

main()