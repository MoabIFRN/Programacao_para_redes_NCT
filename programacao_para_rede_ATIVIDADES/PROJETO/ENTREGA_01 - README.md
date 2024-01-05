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

Atualização do arquivo: 

# README - Bot de Telegram com funcionalidades de Clima, Dólar, Filmes e Mensagem do Dia

Este é um bot de Telegram simples que oferece algumas funcionalidades úteis para os usuários. Ele foi desenvolvido em Python e utiliza a biblioteca `telebot` para interagir com o Telegram e a biblioteca `requests` para fazer requisições a APIs externas.

## Funcionalidades Principais

### 1. Clima
O bot permite que os usuários obtenham informações sobre o clima de uma cidade específica. Por padrão, a cidade configurada é "Natal", mas isso pode ser alterado facilmente no código.

Para utilizar essa funcionalidade, o usuário pode digitar o comando `/clima`.

### 2. Dólar
O bot fornece informações sobre a cotação atual do dólar em relação ao Real (BRL).

Para obter essa informação, o usuário pode utilizar o comando `/dolar`.

### 3. Filmes em Cartaz
Esta funcionalidade permite que os usuários obtenham informações sobre os filmes em cartaz. Os dados são obtidos a partir da API "The Movie Database (TMDb)".

Para visualizar a lista dos filmes em cartaz, o usuário pode usar o comando `/filme`.

### 4. Mensagem do Dia
O bot também oferece uma mensagem motivacional do dia para os usuários. Essa mensagem é pré-definida e não muda.

Para receber a mensagem do dia, o usuário pode usar o comando `/mensagem`.

### 5. Opções Disponíveis
Para ajudar os usuários a entenderem as funcionalidades disponíveis, o bot possui um comando `/opcoes` que lista todas as opções disponíveis.

## Como Utilizar o Bot
Para utilizar o bot, siga os passos abaixo:

1. Inicie uma conversa com o bot no Telegram. O nome de usuário do bot é "bot_token" (neste exemplo).

2. Utilize os comandos mencionados acima (por exemplo, `/clima`, `/dolar`, `/filme`, `/mensagem`) para acessar as diferentes funcionalidades.

3. O bot responderá automaticamente com as informações solicitadas.

Lembre-se de que este é um exemplo simples de um bot de Telegram e pode ser expandido com mais funcionalidades e melhorias. Certifique-se de configurar corretamente a sua chave de API para cada serviço externo usado no código.

**Observação:** É importante que o código seja executado em um ambiente onde o Python e as bibliotecas `telebot` e `requests` estejam instalados e configurados. Certifique-se de ter um token válido do Telegram para o seu bot.
