import socket

HOST = '127.0.0.1'
PORTA = 65431
ENDERECO_SERVIDOR = (HOST, PORTA)

# Mensagem a ser enviada
mensagem = b'Ola, servidor!'

# Cria um socket UDP/IP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Envia a mensagem diretamente para o endereço do servidor
    s.sendto(mensagem, ENDERECO_SERVIDOR)
    print(f"Enviado pelo cliente: {mensagem.decode()}")

    # Espera pela resposta
    dados_recebidos, endereco_servidor = s.recvfrom(1024)

print(f"Recebido de volta do serivdor: {dados_recebidos.decode()}")