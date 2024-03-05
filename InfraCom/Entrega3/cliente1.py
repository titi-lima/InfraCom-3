import socket


HOST = '192.168.100.100'  # Endereço IP do servidor
PORT = 5000         # Porta do servidor

client_soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando socket tcp da familia ipv6
client_soquete.connect((HOST,PORT))#CONECTANDO COM SERVIDOR

#criar dado para enviar
dado = "primeiro dado"
dado = str.enconde(dado); #cofificar em string

#enviar pro servidor
client_soquete.sendall(dado);
#receber
dadoRecebido = client_soquete.recv(1024)#1o24 butes
print("MENSAGEM RECEBIDA", dadoRecebido.decode())


