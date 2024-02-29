import socket
import classeCliente

def main():
    HOST = '192.168.100.100'  # Endereço IP do servidor
    PORT = 5000         # Porta do servidor
    cli1 = Cliente();
    cli1.nome = 'suruagy'
    cli1.settar(HOST,PORT)


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Digite uma mensagem para enviar ao servidor: ")
        client_socket.sendto(message.encode(), (HOST, PORT)) #enviar a mensagem para o servidor com base no seu end IP(host) e porta do dervidor

        response, server_address = client_socket.recvfrom(1024) #tipo um ack
        print(f"Resposta do servidor: {response.decode()}")

if __name__ == "__main__":
    main()