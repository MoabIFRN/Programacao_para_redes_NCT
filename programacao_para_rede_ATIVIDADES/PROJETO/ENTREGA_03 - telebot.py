import telebot
import requests
import socket

TOKEN = '***'  
bot = telebot.TeleBot(TOKEN)

# Configurações para comunicação com o servidor de socket
HOST_SERVER = 'localhost'
SOCKET_PORT = 50000
BUFFER_SIZE = 512
CODE_PAGE = 'utf-8'

# Função para solicitar o endereço IP ao servidor Socket
def solicitar_endereco_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_cliente:
        socket_cliente.sendto("REQUEST_IP".encode(CODE_PAGE), (HOST_SERVER, SOCKET_PORT))
        dados, _ = socket_cliente.recvfrom(BUFFER_SIZE)
        return dados.decode(CODE_PAGE)

# Função para obter o clima
def obter_clima():
    cidade = "Natal"
    chave_api = "bd5e378503939ddaee76f12ad7a97608"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        clima = response.json()
        temperatura = clima['main']['temp']
        return f"A temperatura em {cidade} é de {temperatura}°C."
    else:
        return "Desculpe, não foi possível obter informações sobre o clima."

# Função para obter o valor do dólar
def obter_valor_dolar():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    response = requests.get(url)
    if response.status_code == 200:
        valor = response.json()['rates']['BRL']
        return f"O valor do dólar hoje é de R${valor:.2f}."
    else:
        return "Desculpe, não foi possível obter o valor do dólar."

@bot.message_handler(commands=["clima"])
def clima_command(message):
    resultado = obter_clima()
    bot.send_message(message.chat.id, resultado)

@bot.message_handler(commands=["dolar"])
def dolar_command(message):
    resultado = obter_valor_dolar()
    bot.send_message(message.chat.id, resultado)

@bot.message_handler(commands=["ip"])
def ip_command(message):
    ip = solicitar_endereco_ip()
    bot.send_message(message.chat.id, ip)

@bot.message_handler(commands=["opcoes"])
def opcoes_command(message):
    texto = """
    Escolha uma opção:
    /clima - Informar o clima
    /dolar - Informar o valor do dólar
    /ip - Obter o endereço IP do servidor"""
    bot.send_message(message.chat.id, texto)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = "Escolha uma opção válida: /opcoes - Mostrar opções disponíveis"
    bot.reply_to(message, texto)

bot.polling()
