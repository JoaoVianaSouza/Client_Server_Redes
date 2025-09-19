# Análise Comparativa de Sockets TCP e UDP em Python

Este repositório contém os códigos-fonte desenvolvidos para o trabalho da disciplina de **Redes de Computadores I** da Universidade do Estado do Rio de Janeiro (UERJ).

O projeto consiste em uma aplicação cliente-servidor de "eco" implementada em Python, com versões para os protocolos TCP e UDP. O objetivo é permitir a captura e análise do tráfego de rede para comparar o desempenho e o *overhead* de cada protocolo.

## Arquivos no Repositório

* `servidor_tcp.py`: O servidor que utiliza o protocolo TCP. Ele aguarda uma conexão, recebe uma mensagem e a envia de volta para o cliente.
* `cliente_tcp.py`: O cliente que utiliza o protocolo TCP. Ele se conecta ao servidor, envia uma mensagem e aguarda o eco.
* `servidor_udp.py`: O servidor que utiliza o protocolo UDP. Ele aguarda um datagrama, recebe uma mensagem e o envia de volta para o endereço de origem.
* `cliente_udp.py`: O cliente que utiliza o protocolo UDP. Ele envia um datagrama para o servidor e aguarda o eco.

## Como Executar os Testes

Para executar os testes, você precisará de dois terminais abertos no diretório do projeto. O servidor deve ser iniciado antes do cliente.

#### Teste TCP:

1.  No primeiro terminal, inicie o servidor:
    ```bash
    python servidor_tcp.py
    ```
2.  No segundo terminal, execute o cliente:
    ```bash
    python cliente_tcp.py
    ```

#### Teste UDP:

1.  No primeiro terminal, inicie o servidor:
    ```bash
    python servidor_udp.py
    ```
2.  No segundo terminal, execute o cliente:
    ```bash
    python cliente_udp.py
    ```

**Nota:** Recomenda-se o uso de um sniffer de rede como o **Wireshark** na interface de loopback para capturar e analisar o tráfego gerado durante os testes.
