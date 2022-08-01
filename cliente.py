from classSocket import socketParticipant
import random
import threading

participant = socketParticipant("127.0.0.1",4444)
#participant.send("hola")
print("connect")
global count
count = 0
balance = 1000
#mensaje = participant.resive()
#print("mensaje resive e instanciado por el cliente: ",mensaje)

amount = 0
def main():
    def fun1():
        global z
        z = random.randint(0,1)

        return z

    t1 = threading.Thread(name="hilo_1", target=fun1, args=())
    t1.start()
    t1.join()
    return z

z1 = main()
print(z1)
if(z1 == 1): 
    participant.send("result commit\n")
    balance += amount
elif(z1 == 0):
    participant.send("result rollback\n")
    balance -= amount
mensaje = participant.resive()
print("mensaje resive e instanciado por el cliente: ",mensaje)

