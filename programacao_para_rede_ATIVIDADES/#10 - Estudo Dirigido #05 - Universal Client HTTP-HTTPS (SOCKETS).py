import socket
import os
from urllib.parse import urlparse

def baixar_imagem(url):
    url_parseada = urlparse(url)
    host = url_parseada.netloc
    caminho_imagem = url_parseada.path

    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((host, 80))

    requisicao = f"GET {caminho_imagem} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    socket_cliente.send(requisicao.encode())

    resposta = b""
    while True:
        dados = socket_cliente.recv(1024)
        if not dados:
            break
        resposta += dados

    indice_inicio = resposta.find(b"\r\n\r\n") + 4

    nome_arquivo = os.path.basename(caminho_imagem)
    with open(nome_arquivo, "wb") as arquivo_imagem:
        arquivo_imagem.write(resposta[indice_inicio:])

    print(f"Imagem baixada com sucesso. Salva como {nome_arquivo}")

    socket_cliente.close()

if __name__ == "__main__":
    url = input("Informe a URL completa da imagem: ")

    baixar_imagem(url)
