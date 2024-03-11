# Segunda Entrega

## Arquivos

- `client.py`: Cliente. Lê um arquivo, envia para o servidor e recebe o arquivo de volta.
- `server.py`: Servidor. Recebe um arquivo do cliente, salva e envia de volta para o cliente.
- `rd3.py`: Classe responsável pelo serviço de transmissão confiável. Declara uma classe que é instanciada tanto pelo cliente quanto pelo servidor.
- `test_file.txt` e `imagem.png`: Arquivos de teste que podem ser usados para testar a transferência de arquivos.

## Como usar

1. Execute o servidor:
    ```sh
    python server.py
    ```

2. Em outro terminal, execute o cliente e siga as instruções para enviar um arquivo:
    ```sh
    python client.py
    ```

O cliente enviará o arquivo para o servidor (guardado em received_file no diretório que foi rodado), que por sua vez enviará o arquivo de volta para o cliente (guardado em received_back_file + extensão no diretório que foi rodado).

## Como testar a perda de pacotes

1. Vá ao arquivo rd3.py

2. Substitua o nome da função 
    ```python
    def udt_send(self, data):
        addr = (self.addrName, self.addrPort)

        print('sending data to addr:', addr)

        if not isinstance(data, bytes):
            data = data.encode()

        # if random.random() < 0.2:
        #     print('Packet lost!')
        #     return

        self.udp.sendto(data, addr)

    ```

    por 

    ```python
    def udt_send(self, data):
        addr = (self.addrName, self.addrPort)

        print('sending data to addr:', addr)

        if not isinstance(data, bytes):
            data = data.encode()

        if random.random() < 0.2:
             print('Packet lost!')
             return

        self.udp.sendto(data, addr)
    ```

    isso irá causar uma probabilidade de 20% de perda de pacotes, você pode aumentar essa probabilidade, mas note que números mais altos resultam em uma transmissão muito lenta
4. Execute os passos mostrados anteriormente para testar