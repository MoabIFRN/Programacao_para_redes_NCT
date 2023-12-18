import telebot
import requests

TOKEN = 'SEU_TOKEN_AQUI'

bot = telebot.TeleBot(TOKEN)

# Função para obter informações sobre o clima usando a API OpenWeatherMap
def obter_clima():
    cidade = "SaoPaulo"  # Substitua pela cidade desejada
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric"
    
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

# Função para obter indicação de lançamento de filme
def obter_lancamento_filme():
    url = "https://api.themoviedb.org/3/movie/upcoming?api_key=API_KEY&language=pt-BR&page=1"
    
    response = requests.get(url)
    if response.status_code == 200:
        if response.json()['results']:
            filme = response.json()['results'][0]['title']
            return f"O próximo filme no cinema é: {filme}"
        else:
            return "Não há informações sobre novos filmes no momento."
    else:
        return "Desculpe, não foi possível obter informações sobre filmes."

# Função para enviar uma mensagem do dia
def enviar_mensagem_do_dia():
    return "Aqui está a mensagem do dia: 'Aproveite cada momento da sua vida!'"

# Handlers dos comandos do bot
@bot.message_handler(commands=["clima"])
def clima_command(message):
    resultado = obter_clima()
    bot.send_message(message.chat.id, resultado)

@bot.message_handler(commands=["dolar"])
def dolar_command(message):
    resultado = obter_valor_dolar()
    bot.send_message(message.chat.id, resultado)

@bot.message_handler(commands=["filme"])
def filme_command(message):
    resultado = obter_lancamento_filme()
    bot.send_message(message.chat.id, resultado)

@bot.message_handler(commands=["mensagem"])
def mensagem_command(message):
    resultado = enviar_mensagem_do_dia()
    bot.send_message(message.chat.id, resultado)

@bot.message_handler(commands=["opcoes"])
def opcoes_command(message):
    texto = """
    Escolha uma opção:
    /clima - Informar o clima
    /dolar - Informar o valor do dólar
    /filme - Indicação de lançamento de filme no cinema
    /mensagem - Receber uma mensagem do dia"""
    bot.send_message(message.chat.id, texto)

# Verifica mensagens para opções inválidas
def verificar(message):
    return True

@bot.message_handler(func=verificar)
def responder(message):
    texto = """
    Escolha uma opção válida:
    /opcoes - Mostrar opções disponíveis"""
    bot.reply_to(message, texto)

# Inicia o bot
bot.polling()

