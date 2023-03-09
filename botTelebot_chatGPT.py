import telebot
import openai

TOKEN = '' # здесь вставить ключ от BotFather
openai.api_key = "" # здесь вставить ключ от openai api_key


bot = telebot.TeleBot(TOKEN)

# Определение команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ChatGPT на русском языке. Введите текст, и я попытаюсь сгенерировать продолжение для вас.")

# Определение обработчика текстовых сообщений
@bot.message_handler(func=lambda message: True)
def generate_text(message):
    # Получение текста из сообщения пользователя
    user_text = message.text
    # Определение параметров генерации текста
    prompt = f"{user_text}\n" # на основании данного текста бот отвечает
    model = "text-davinci-003" # текстовая модель можно выбрать и другую
    temperature = 0,58 # чем меньше это значение, тем более обычные ответы, от 0 до 1
    max_tokens = 1024
    # Вызов API OpenAI для генерации продолжения текста
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    # Получение сгенерированного текста из ответа API OpenAI
    bot_response = response.choices[0].text
    bot.reply_to(message, bot_response)

bot.polling()