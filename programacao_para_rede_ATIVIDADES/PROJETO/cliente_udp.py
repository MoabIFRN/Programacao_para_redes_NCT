import socket

HOST_SERVER = 'localhost'   # Definindo o IP do servidor
SOCKET_PORT = 50000         # Definindo a porta
BUFFER_SIZE = 512           # Definindo o tamanho do buffer
CODE_PAGE   = 'utf-8'       # Definindo a página de códigos de caracteres-

MAX_LISTEN  = 1             # Definindo o máximo de conexões enfileiradas 

#Obtém o texto para enviar
texto = input("Digite o texto para enviar: ")

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP_PORTA = (HOST_SERVER, SOCKET_PORT)
dados = texto.encode(CODE_PAGE)

socket_cliente.sendto(dados, IP_PORTA)
print("Dados enviados!")

dados, endereco_servidor = socket_cliente.recvfrom(BUFFER_SIZE)
print(f"Resposta do servidor: {dados.decode(CODE_PAGE)}")

socket_cliente.close()
