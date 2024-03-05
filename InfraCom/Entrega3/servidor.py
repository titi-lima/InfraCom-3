import socket

HOST = '192.168.100.100'  # Endereço IP do servidor
PORT = 5000         # Porta que o servidor irá escutar

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #familia ipv6 e protocolo tcp
soquete.bind((HOST,PORT))#PARAMETRO UNICO, CRIAR ENDERECO DO SOCKET
soquete.listen() #modo de escuta, aguarda cliente
print("esperando conexao")


conexao,endereco = soquete.accept()
#aqui, lockar uma thread para evitar superposição de processos na mesma porta do mesmo servidor
print("concectado em", endereco)


while True:
  dado = conexao.recv(1024)#receber ate 1024 bytes
  if not dado:
    print("fechando conexao")
    conexao.close()
    break
  
conexao.sendall(dado)
#aqui, desbloquear a thread, pois a conexão do servidor foi concluída



