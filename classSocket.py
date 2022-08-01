import socket
import random



class socketParticipant :

    participant = socket.socket()
    def __init__(self,host,port):
        self.participant.connect((host, port))
        

    def send(self, mensaje):
        self.participant.send(mensaje.encode())
        print("mensaje enviado: ",mensaje)

    def resive(self):
        datos = self.participant.recv(4096)
        mensaje = datos.decode('UTF-8')
        print("mensaje resivido: ",mensaje)
        return mensaje

    def decidir(self ):
        print("fun")