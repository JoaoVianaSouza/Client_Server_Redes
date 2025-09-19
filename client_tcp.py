import socket

HOST = '127.0.0.1'
PORTA = 65432  # Porta a ser usada

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORTA))

    s.listen()
    print(f"Servidor TCP escutando em {HOST}:{PORTA}")

    conn, addr = s.accept()

    with conn:
        print(f"Conectado por {addr}")
        while True:
            dados = conn.recv(1024)
            if not dados:
                break

            print(f"Recebido: {dados.decode()}")

            # Envia os mesmos dados de volta para o cliente (eco)
            conn.sendall(dados)
            print(f"Enviado de volta: {dados.decode()}")