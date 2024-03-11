from rdt3 import RDT
import socket

class Sala:
  def __init__(self,nome):
       self.agenda = [["", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", "", ""]]
       self.nome = nome

sala1= Sala('E101')
sala2= Sala('E102')
sala3= Sala('E103')
sala4= Sala('E104')
sala5= Sala('E105')

salasList = [sala1, sala2, sala3, sala4, sala5]

class Cliente:
  def __init__(self,clientPort,nome,flag):
        self.endCliente = clientPort
        self.nome = nome
        self.flag = flag

clients = []

def connect(clienteOBJ,clientlist,host,port,sala,dia,hora):
            
            tamanho = clientlist.length
            clientlist[tamanho +1] = clienteOBJ #atualiza vetor

            #ver se a sala está ocupada

            if sala.agenda[dia][hora]:#sala ocupada
                 print("essa sala já está ocudada nesse dia, nessa hora")
            else:
                
                print(clienteOBJ.nome, "reservou a sala")
                
def reserve(nome, numero, dia, horario):
    if nome in clients:
        for sala in salasList:
            if sala.nome == numero and sala.agenda[dia][horario] == "":
                sala.agenda[dia][horario] = nome
            else:
                 print("retornar que a sala tá ocupada")
    else:
         print("Sei lá retorna que a pessoa não tá conectada?")

def cancel(nome, numero, dia, horario):
    for sala in salasList:
        if sala.nome == numero and sala.agenda[dia][horario] == nome:
            sala.agenda[dia][horario] = ""
        else:
            print("retornar que a sala tá ocupada por outra pessoa")

def check(numero, dia):
    for sala in salasList:
        if sala.nome == numero:
            sala.agenda[dia][horario] = ""
            break
        else:
            print("retornar que a sala tá ocupada por outra pessoa")
    print("retornar que não achou a sala")

def main():
    server = RDT('server', addPort=13009)
    
    while True:
        print("Server receiving")
        server.reset_num_seq()
        rcvpkt, addr = server.rdt_rcv() #iniciando modo de escuta
        if (rcvpkt.split(" ")[0] == "connect"):
            print("Server received connection request")
            #TODO: fazer função que enviar que recebe uma mensagem como parametro e envia ela para todos os usuarios conectados
            clients.append(Cliente(addr, rcvpkt.split(" ")[1], True))
            server.rdt_send("Connected", addr)
        elif (rcvpkt.split(" ")[0] == "check"):
            print("Server received check request")
            check(rcvpkt.split(" ")[1], rcvpkt.split(" ")[2])
        
        

