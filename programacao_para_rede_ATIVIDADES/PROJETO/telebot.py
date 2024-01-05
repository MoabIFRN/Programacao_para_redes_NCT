import telebot
import requests

TOKEN = '***'

bot = telebot.TeleBot(TOKEN)

def obter_clima():
  cidade = "Natal"
  chave_api = "bd5e378503939ddaee76f12ad7a97608"  # Sua chave de API
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




# Função Filmes
bot_token = "6952533718:AAH5ya3iAzqP3OnEXL1lAu-5TF90_fRlM_I"
api_key = '6275a571164083ab21055947b4aa8bd7'
bot = telebot.TeleBot(bot_token)

def obter_filmes_em_cartaz():
    url_base = "https://api.themoviedb.org/3/movie/now_playing"
    parametros = {
      "api_key": api_key,
"api_key": '6275a571164083ab21055947b4aa8bd7',
        "language": "pt-BR",
        "page": 1
    }
    resposta = requests.get(url_base, params=parametros)
    if resposta.status_code == 200:
        dados = resposta.json()
        filmes = dados['results'][:10]  # Obtém os 10 primeiros filmes
        resposta_texto = "Filmes em cartaz:\n"
        for filme in filmes:
            resposta_texto += f"{filme['title']} - {filme['overview']}\n\n"
        return resposta_texto
    else:
        return "Erro ao acessar a API"
        

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
    resultado = obter_filmes_em_cartaz()
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
