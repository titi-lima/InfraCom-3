import socket
import random


class RDT:
    # Construtor da classe. Inicializa o socket UDP, define o tipo (cliente ou servidor),
    # o endereço e a porta de comunicação, e inicializa os números de sequência para controle.
    def __init__(self, type: str, addrPort: int = 5000, addrName: str = "127.0.1.1"):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addrPort = addrPort
        self.addrName = addrName
        self.type = type
        self.num_seq_c = 0
        self.num_seq_s = 0

        # vincula o socket do server a porta especificada.
        self.udp.bind((self.addrName, addrPort))

    def __del__(self):
        self.udp.close()

    # Cria um pacote de dados encapsulando os dados e o número de sequência em uma string codificada.
    def make_pkt(self, data, num_seq):
        return str({"data": data, "num_seq": num_seq}).encode()

    # Reseta os números de sequência
    def reset_num_seq(self):
        self.num_seq_c = 0
        self.num_seq_s = 0

    def close(self):
        self.__del__()

    # Envia dados utilizando o protocolo UDP para o endereço e porta especificados.
    def udt_send(self, data, addr=None):
        if addr == None:
            addr = (self.addrName, self.addrPort)  # (HOST, PORTA CLIENT)

        if not isinstance(data, bytes):
            data = data.encode()

        self.udp.sendto(data, addr)

    # Recebe dados utilizando o protocolo UDP. Se for cliente, apenas recebe,
    # se for servidor, atualiza o endereço e porta do remetente para responder.
    def udt_rcv(self):
        bytes_read, addr = self.udp.recvfrom(4096)
        self.addrName = addr[0]
        self.addrPort = addr[1]
        addr = (self.addrName, self.addrPort)

        return (eval(bytes_read.decode()), addr)

    # Envia dados de forma confiável, aguardando ACK do receptor. Se não receber ACK,
    # reenvia os dados após um timeout.
    def rdt_send(self, data, addr=None):
        attempts = 0
        max_attempts = 5
        timeout = 2  # Starting timeout period
        self.udp.settimeout(timeout)

        while attempts < max_attempts:
            print(
                "Sending data", data, "to", addr, "with sequence number", self.num_seq_c
            )
            sndpkt = self.make_pkt(data, self.num_seq_c)
            self.udt_send(sndpkt, addr)
            try:
                ack_pkt, _ = self.rdt_rcv("wait_ack")
                if (
                    ack_pkt
                    and ack_pkt["num_seq"] == self.num_seq_c
                    and ack_pkt["data"] == b"ACK"
                ):
                    # Ack received, update sequence number for next transmission
                    self.num_seq_c = 1 - self.num_seq_c
                    return
            except socket.timeout:
                # Timeout occurred, prepare to retry
                attempts += 1
                timeout += 1  # Increment timeout to allow for longer wait
                self.udp.settimeout(timeout)

        self.udp.settimeout(None)  # Reset timeout to default
        if attempts >= max_attempts:
            raise Exception("Failed to send data after maximum attempts.")

    def rdt_rcv(self, state="null"):
        while True:
            try:
                pkt, addr = self.udt_rcv()
                # Check for correct sequence number and ACK, if waiting for ACK
                if (
                    state == "wait_ack"
                    and pkt["data"] == b"ACK"
                    and pkt["num_seq"] == self.num_seq_c
                ):
                    return pkt, addr
                # If receiving data, check sequence number and send ACK if correct
                elif state != "wait_ack" and pkt["num_seq"] == self.num_seq_s:
                    ack_pkt = self.make_pkt(b"ACK", self.num_seq_s)
                    self.udt_send(ack_pkt, addr)
                    self.num_seq_s = (
                        1 - self.num_seq_s
                    )  # Update sequence number for next reception
                    return pkt, addr
                # If packet is duplicate or out of order, ignore or handle accordingly
            except socket.timeout:
                # If we're waiting for ACK and it times out, let the sender handle the timeout
                if state == "wait_ack":
                    return None, None
