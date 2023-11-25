Aplicação Cliente-Servidor UDP em Python

Este é um simples exemplo de comunicação entre um cliente e um servidor usando sockets UDP (User Datagram Protocol) em Python.
Funcionalidades:

    Servidor:
        Cria um socket e aguarda a conexão do cliente.
        Recebe dados do cliente, decodifica e exibe na tela.
        Envia uma resposta ao cliente após receber os dados.

    Cliente:
        Solicita ao usuário um texto para enviar ao servidor.
        Cria um socket, codifica os dados e envia ao servidor.
        Aguarda a resposta do servidor e a exibe na tela.

Como Utilizar:

    Servidor:
        Execute o script do servidor (servidor.py).
        Aguarde a conexão do cliente.
        Após receber os dados do cliente, envia uma resposta.

    Cliente:
        Execute o script do cliente (cliente.py).
        Insira um texto quando solicitado para enviar ao servidor.
        Aguarde a resposta do servidor exibida na tela.

Observações:

    Certifique-se de executar primeiro o servidor antes do cliente.
    Ambos cliente e servidor estão configurados para se comunicarem localmente na porta 5000 e no endereço IPv4 '127.0.0.1' (localhost).
