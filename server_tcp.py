import socket

HOST = '127.0.0.1'  # O endereço do servidor
PORTA = 65432  # A mesma porta usada pelo servidor

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta-se ao servidor
    s.connect((HOST, PORTA))

    # Mensagem a ser enviada
    mensagem = b'Ola, mundo TCP!'

    # Envia a mensagem
    s.sendall(mensagem)
    print(f"Enviado: {mensagem.decode()}")

    # Espera pela resposta do servidor (o eco)
    dados_recebidos = s.recv(1024)

print(f"Recebido de volta: {dados_recebidos.decode()}")