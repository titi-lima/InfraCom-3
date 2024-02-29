# InfraCom-3


Terceira Etapa: Sistema de gerenciamento de reservas de salas com paradigma cliente-servidor

(4,5 pontos) Implementação do sistema de reservas, exibido por linha de comando. Apesar do reaproveitamento das etapas anteriores, o histórico da execução dos algoritmos não deve ser exibido nessa etapa, apenas a aplicação como descrita nesse documento e mantendo o uso do rdt3.0. Prazo máximo de entrega: 12/03/2024 às 23:59

Obs.: Na terceira entrega do projeto é necessário que o sistema funcione para mais de um cliente simultaneamente, ou seja, deverão ser abertos o terminal do servidor e ao menos dois terminais de clientes sem que ocorra interrupção do funcionamento.

A implementação deverá ser realizada conforme os requisitos a seguir:

O socket UDP de cada cliente e do servidor deverá contar com transmissão confiável, implementada em camada de aplicação segundo o rdt 3.0 que consta no livro “Redes de Computadores e a Internet” do Kurose.


!!O que está em vermelho não é negociável!!

Os usuários conectados deverão fazer login no sistema em seus respectivos clientes e poderão interagir com o servidor, executando comandos e verificando informações desejadas.

Um participante poderá conhecer previamente outro usuário através de uma lista de contatos local de cada um a partir de solicitação via comando a ser descrito posteriormente. 
