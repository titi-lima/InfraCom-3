# InfraCom-3


Terceira Etapa: Sistema de gerenciamento de reservas de salas com paradigma cliente-servidor

(4,5 pontos) Implementação do sistema de reservas, exibido por linha de comando. Apesar do reaproveitamento das etapas anteriores, o histórico da execução dos algoritmos não deve ser exibido nessa etapa, apenas a aplicação como descrita nesse documento e mantendo o uso do rdt3.0. Prazo máximo de entrega: 12/03/2024 às 23:59

Obs.: Na terceira entrega do projeto é necessário que o sistema funcione para mais de um cliente simultaneamente, ou seja, deverão ser abertos o terminal do servidor e ao menos dois terminais de clientes sem que ocorra interrupção do funcionamento.

A implementação deverá ser realizada conforme os requisitos a seguir:

O socket UDP de cada cliente e do servidor deverá contar com transmissão confiável, implementada em camada de aplicação segundo o rdt 3.0 que consta no livro “Redes de Computadores e a Internet” do Kurose.


!!O que está em vermelho não é negociável!!

Os usuários conectados deverão fazer login no sistema em seus respectivos clientes e poderão interagir com o servidor, executando comandos e verificando informações desejadas.

Um participante poderá conhecer previamente outro usuário através de uma lista de contatos local de cada um a partir de solicitação via comando a ser descrito posteriormente. 
![Captura de tela 2024-02-29 150028](https://github.com/mms-11/InfraCom-3/assets/140762703/e51e3d8e-0630-4f99-a83a-71ccc2338c3a)
![Captura de tela 2024-02-29 150117](https://github.com/mms-11/InfraCom-3/assets/140762703/222aed2f-8def-4596-bce5-1b8756d91a5e)

Quando um usuário se conectar à sala, os outros usuários deverão receber uma mensagem de alerta da nova presença (ex: João está avaliando reservas!). 

Após estar conectado, qualquer reserva realizada/cancelada deverá ser informada para todos os outros usuários conectados (ex: Pedro [192.168.100.100:5890] reservou a sala E101 na Terça 11h). O servidor  também deverá retornar para quem reservou/cancelou a sala a seguinte mensagem: (ex: Você [192.168.100.100:5890] reservou a sala E101]

Todas as reservas são de apenas 1 hora e somente podem ser realizadas entre segunda e sexta-feira das 8:00 até às 17:00. 

Considerem que serão usadas 5 salas de reunião para esse evento: E101 até E105.

Dois usuários não podem se conectar à sala utilizando o mesmo nome e não podem
reservar a mesma sala no mesmo horário.

Sair do aplicativo: Ao usar esse comando, o usuário deve se desconectar e o socket será encerrado. Além disso, todos os usuários conectados devem receber um aviso a respeito da saída desse participante (ex: Lara saiu do sistema de reservas!). 



Reservar uma sala: Ao usar esse comando, o usuário especifica a sala que deseja reservar, em que dia da semana do evento (Seg-Sex) e o horário de início da reserva. Ao solicitar uma reserva o sistema deve verificar se o horário selecionado está disponível e em caso positivo confirmar a reserva, caso contrário indicar a indisponibilidade e quem é o dono da reserva desejada.

Obs.: Para fins de simplicidade os horários devem ser sempre horários fechados, como por exemplo 8, que indica uma reserva das 8 até às 8:59 da manhã.
Obs1.: É indicado que haja uma padronização ao especificar os dias da semana, por exemplo “Seg”, “Ter”, “Sex”. Ou adaptar seu código de modo que ele entenda que “seg == Seg”
Obs2.: Como já mencionado anteriormente, todos os usuários conectados deverão receber um indicativo da nova reserva realizada e a informação de que a sala agora está indisponível, atualizando a tabela de disponibilidade no servidor

Cancelar reserva: Ao usar esse comando, o usuário especifica a sala, o dia e o horário de início da reserva que deseja cancelar. É fundamental que o servidor verifique se o usuário que solicitou o cancelamento é de fato o dono da reserva, caso não seja deverá ser apresentada uma mensagem de erro.

Obs.: Como já mencionado anteriormente, todos os usuários conectados deverão receber um indicativo do cancelamento e a informação de que a sala agora está disponível, seguindo o modelo de informação já exemplificado anteriormente (constar endereço do dono da reserva) e atualizando a tabela de disponibilidade no servidor.

Verificar disponibilidade em sala específica: Ao usar esse comando, o usuário especifica a sala e o dia da semana que deseja realizar a reserva, a partir disso o servidor deverá retornar o indicativo de quais horários estão disponíveis. (ex: Usuário digita -> check E103 Quarta e deverá receber o seguinte retorno: -> E103 Qua -> 8 10 12 15 17)





