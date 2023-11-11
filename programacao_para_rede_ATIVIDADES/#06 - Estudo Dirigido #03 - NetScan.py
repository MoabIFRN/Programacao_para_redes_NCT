import socket

def verificar_porta(host, port, protocolo, descricao):
    try:
        # Criar um socket para a conexão
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Configurar um tempo limite curto para a conexão

        # Tentar conectar à porta
        resultado = sock.connect_ex((host, port))

        # Determinar o status da porta
        if resultado == 0:
            status = 'Aberta'
        else:
            status = 'Fechada'

        # Exibir o resultado na tela
        print(f"Porta {port}: Protocolo: {protocolo}: ({descricao})/ Status: Responde ({status})")

        sock.close()  # Fechar o socket

    except socket.error:
        print(f"Erro ao conectar à porta {port}")

def main():
    # Solicitar o endereço do host
    host = input("Digite o endereço do host: ")

    try:
        # Tentar obter o endereço IP do host
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Não foi possível resolver o nome do host.")
        return

    # Dados incorporados no código
    dados = """
    Porta   Protocolo                       Descrição
    0       TCP,UDP                         Reservada. Fora de Serviço
    1       TCP,UDP                         TCPMUX (Serviço de porta TCP multiplexador) Oficial
    5       TCP,UDP                         RJE (Remote Job Entry - Entrada de trabalho remoto) Oficial
    7       TCP,UDP                         ECHO protocol (Serviço Echo) Oficial
    9       TCP,UDP                         DISCARD protocol (Serviço zero para teste de conexão) Oficial
    11      TCP,UDP                         SYSTAT protocol (Serviço de Estado do Sistema para listar as portas conectadas) Oficial
    13      TCP,UDP                         DAYTIME protocol (Envia data e hora para a máquina requerente) Oficial
    17      TCP,UDP                         QOTD protocol (Envia a citação do dia para a máquina conectada) Oficial
    18      TCP,UDP                         Message Send Protocol (Protocolo de envio de mensagem) Oficial
    19      TCP,UDP                         CHARGEN protocol (Character Generator Protocol - Protocolo de geração de caracter) Oficial
    20      TCP                             FTP (File Transfer Protocol - Protocolo de transferência de arquivo) - Porta de dados do FTP Oficial
    21      TCP                             FTP (File Transfer Protocol - Protocolo de transferência de arquivo) - Porta do Protocolo de Transferência de Arquivos Oficial
    22      TCP,UDP                         SSH (Secure Shell - Shell seguro) - Usada para logins seguros, transferência de arquivos e redirecionamento de porta Oficial
    23      TCP,UDP                         Telnet protocol - Comunicação de texto sem encriptação Oficial
    25      TCP,UDP                         SMTP (Simple Mail Transfer Protocol - Protocolo simples de envio de e-mail) - usada para roteamento de e-mail entre servidores (Atualmente é utilizada a porta 587,conforme Comitê Gestor da Internet no Brasil CGI.br Oficial
    26      TCP,UDP                         RSFTP - protocolo similar ao FTP Não-oficial
    ... (continuação)
    """

    # Separando as linhas
    linhas = dados.strip().split('\n')

    # Iterando pelas linhas e adicionando portas à lista
    portas_e_descricoes = []
    for linha in linhas[2:]:  # Ignorar as duas primeiras linhas de cabeçalho
        dados = linha.split(None, 2)  # Limitar a divisão a duas partes
        if len(dados) == 3:
            porta, protocolo, descricao = int(dados[0]), dados[1], dados[2]
            portas_e_descricoes.append((porta, protocolo, descricao))


    # Verificar cada porta na lista
    for porta, protocolo, descricao in portas_e_descricoes:
        verificar_porta(ip, porta, protocolo, descricao)

if __name__ == "__main__":
    main()




