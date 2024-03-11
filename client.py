from rdt3 import RDT
import threading
import socket
from server import Cliente
from server import Sala

clientPort = 5000

while True:
    try:
        clientRcv = RDT('client', addrPort=clientPort)
        break
    except:
        clientPort += 1
        
lock = threading.Lock()

def rcv_data():
    while True:
        clientRcv.reset_num_seq()
        rcv_pkt = clientRcv.rdt_rcv()
        print(rcv_pkt)

def snd_data():
    print("Qual o seu nome?")
    nome = input()
    connectString = "connect " + nome
    clientRcv.rdt_send(connectString)
    while True:
        print("Escolha sua operação:")
        print("Verificar disponibilidade em sala específica - 1")
        print("Reservar sala - 2")
        print("Cancelar reserva - 3")
        print("Exibir lista de usuários - 4")
        print("Sair - 5")
        data = input('\n')
        #print('\n')
        if data == 1:
            sala = input("Digite o número da sala: ")
            string = "check " + sala
            clientRcv.rdt_send(string)     #:)
        elif data == 2:
            sala = input("Digite o número da sala: ")
            dia = input("Digite o dia desejado: ")
            hora = input ("Digite o horário desejado: ")
            string = "reservar " + sala + " " + dia + " " + hora
            clientRcv.rdt_send(string)
        elif data == 3:
            sala = input("Digite o número da sala: ")
            dia = input("Digite o dia da reserva: ")
            hora = input ("Digite o horário da reserva: ")
            string = "cancelar " + sala + " " + dia + " " + hora
            clientRcv.rdt_send(string)
        elif data == 4:
            string = "list"
            clientRcv.rdt_send(string)
        elif data == 5:
            string = "bye"
            clientRcv.rdt_send(string)
        clientRcv.reset_num_seq()
    
def main():
    threading.Thread(target=snd_data).start()
    threading.Thread(target=rcv_data).start()
            
if __name__ == "__main__":
    main()
