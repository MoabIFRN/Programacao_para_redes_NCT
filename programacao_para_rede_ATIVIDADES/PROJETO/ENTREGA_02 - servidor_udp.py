import socket
HOST_SERVER = 'localhost'   # Definindo o IP do servidor
SOCKET_PORT = 50000         # Definindo a porta
BUFFER_SIZE = 512           # Definindo o tamanho do buffer
CODE_PAGE   = 'utf-8'       # Definindo a página de códigos de caracteres-

MAX_LISTEN  = 1             # Definindo o máximo de conexões enfileiradas 

# Criação do socket, IPv4 e UDP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP e porta associados ao servidor
IP_PORTA = (HOST_SERVER, SOCKET_PORT )
socket_servidor.bind(IP_PORTA)

# Recebendo os dados
print("Esperando dados do cliente...")
dados, endereco_cliente = socket_servidor.recvfrom(BUFFER_SIZE)

# Decodifica os dados
texto = dados.decode(CODE_PAGE)

# Mostra os dados
print(f"Dados recebidos de {endereco_cliente}: {texto}")

# Codifica e envia a resposta
dados = "Obrigado pelos dados!".encode(CODE_PAGE)
socket_servidor.sendto(dados, endereco_cliente)

# Libera os recursos do socket
socket_servidor.close()
