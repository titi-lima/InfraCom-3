import socket


HOST = '192.168.100.100'  # Endereço IP do servidor
PORT = 5000         # Porta do servidor


def settar(endFamilia,tipoProtocolo,nome):
        return socket.socket(endFamilia, tipoProtocolo) #criando socket tcp da familia ipv6




def connectar(nome_do_usuario,socketlist,host,port):
        for soq in socketList:
                if(soq.nome.equals(nome_do_usuario)):
                    soq.connect((host,port)) #aqui conecta com o servidor
                    soq.flag = True
         
                    #criar dado para enviar
                    dado = "primeiro dado"
                    dado = str.enconde(dado); #cofificar em string

                    #enviar pro servidor
                    soq.sendall(dado);

                     #receber
                    dadoRecebido = soq.recv(1024)#1024 butes
                    print("MENSAGEM RECEBIDA", dadoRecebido.decode())

def list():
#listar os usuarios conectados no momento    
       for soq in socketList:
            if soq.flag == True:
                   print(soq.nome)             



 



client_soquete1 = settar(socket.AF_INET, socket.SOCK_STREAM)
client_soquete1.nome = 'Joao'

client_soquete2 = settar(socket.AF_INET, socket.SOCK_STREAM)
client_soquete2.nome = 'Maria'

#criando lista de 2 sockets
socketList = [client_soquete1, client_soquete2]

#conectar usuarios
connectar('Joao',socketList,HOST,PORT)
connectar('Maria', socketList, HOST,PORT)









