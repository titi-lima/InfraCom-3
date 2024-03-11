import socket


HOST = '192.168.100.100'  # Endereço IP do servidor
PORT = 5000         # Porta do servidor
PORT2 = 5500 

class Sala:

  def __init__(self,nome, status,dia,horario,usuario):
       self.status = status
       self.dia = dia
       self.horario = horario
       self.usuario = usuario
       self.nome = nome

class Conexao:

  def __init__(self,endFamilia,tipoProtocolo,nome,flag):
       
        self.end = endFamilia
        self.proto = tipoProtocolo
        self.nome = nome
        self.flag = flag
        self.soq = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


  def connectar(nome_do_usuario,socketlist,host,port):
        for soq in socketlist:
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

def list(socketlist):
#listar os usuarios conectados no momento    
       for soq in socketlist:
            if soq.flag == True:
                   print(soq.nome) 

def reservar(sala,dia,horario,soq):
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
       for soq in socketlist:
              if(soq.name.equals(nome)):
                     soq.close()
                     return print(nome,"Encerrou a conexao")
       
 



client_soquete1 = Conexao(socket.AF_INET, socket.SOCK_STREAM,'Joao', False)
client_soquete2 = Conexao(socket.AF_INET, socket.SOCK_STREAM, 'Maria', False)




#criando lista de 2 sockets
socketList = [client_soquete1, client_soquete2]

#criando lista de 5 salas
sala1= Sala('E101',False,0,0,None)
sala2= Sala('E101',False,0,0,None)
sala3= Sala('E101',False,0,0, None)
sala4= Sala('E101',False,0,0,None)
sala5= Sala('E101',False,0,0, None)

salasList = [sala1,sala2,sala3,sala4,sala5]

#conectar usuarios
client_soquete1.connectar('Joao',socketList,HOST,PORT)
client_soquete2.connectar('Maria', socketList, HOST,PORT2)











