import socket

def main():
    HOST = '127.0.0.1'  # Endereço IP do servidor
    PORT = 5000         # Porta que o servidor irá escutar

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print("Servidor pronto para receber conexões.")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Recebido de {client_address}: {data.decode()}")

        # Simula o envio de uma resposta(Ack do lado receptor)
        response = "Mensagem recebida pelo servidor."
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    main()