import socket

HOST = '127.0.0.1'
PORTA = 65431

# Cria um socket UDP/IP
# SOCK_DGRAM indica que será um socket UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORTA))
    print(f"Servidor UDP escutando em {HOST}:{PORTA}")

    while True:
        # Recebe dados do cliente. recvfrom também retorna o endereço do remetente.
        dados, endereco_cliente = s.recvfrom(1024)

        if not dados:
            break

        print(f"Recebido de {endereco_cliente}: {dados.decode()}")

        # Envia os dados de volta para o endereço do cliente que os enviou
        s.sendto(dados, endereco_cliente)
        print(f"Enviado de volta para {endereco_cliente}: {dados.decode()}")