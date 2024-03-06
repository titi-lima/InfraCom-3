import socket


HOST = '192.168.100.100'  # Endereço IP do servidor
PORT = 5000         # Porta do servidor
PORT2 = 5500 

def sala(self,nome, status,dia,horario,usuario):
       self.status = status
       self.dia = dia
       self.horario = horario
       self.usuario = usuario
       self.nome = nome

def settar(endFamilia,tipoProtocolo,nome):
        return socket.socket(endFamilia, tipoProtocolo) #criando socket tcp da familia ipv6




def connectar(nome_do_usuario,socketlist,host,port):
        for soq in socketList:
                if(soq.nome.equals(nome_do_usuario)):
                    soq.connect((host,port)) #aqui conecta com o servidor
                    soq.flag = True
                    print(soq.name, 'Entrou no sistema de reservas \n')
         
                    #criar dado para enviar
                    dado = "primeiro dado"
                    dado = str.enconde(dado) #cofificar em string

                    #enviar pro servidor
                    soq.sendall(dado)

                     #receber
                    dadoRecebido = soq.recv(1024)#1024 butes
                    print("MENSAGEM RECEBIDA", dadoRecebido.decode())

def list():
#listar os usuarios conectados no momento    
       for soq in socketList:
            if soq.flag == True:
                   print(soq.nome) 

def reservar(sala,dia,horario,socketList,soq):
       #verificar se a sala está ocupada 
       if sala.flag == True:
              return print("A sala", sala.nome, "já está ocupada")    

       #verificar se o usuario está conectado 
       if soq.flag == True:
              #reservar a sala
              sala.flag = True
              sala.dia = dia
              sala.horario = horario
              return print(soq.nome, 'reservou a sala ', sala.nome, 'às', horario, 'da', dia)

def bye(nome,socketlist):
       for soq in socketList:
              if(soq.name.equals(nome)):
                     soq.close()
                     return print(nome,"Encerrou a conexao")
       
 



client_soquete1 = settar(socket.AF_INET, socket.SOCK_STREAM)
client_soquete1.nome = 'Joao'

client_soquete2 = settar(socket.AF_INET, socket.SOCK_STREAM)
client_soquete2.nome = 'Maria'

#criando lista de 2 sockets
socketList = [client_soquete1, client_soquete2]

#criando lista de 5 salas
sala1= sala('E101',False,0,0)
sala2= sala('E101',False,0,0)
sala3= sala('E101',False,0,0)
sala4= sala('E101',False,0,0)
sala5= sala('E101',False,0,0)

salasList = [sala1,sala2,sala3,sala4.sala5]

#conectar usuarios
connectar('Joao',socketList,HOST,PORT)
connectar('Maria', socketList, HOST,PORT2)











