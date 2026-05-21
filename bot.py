import telebot
from groq import Groq

client = Groq(api_key="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")
bot = telebot.TeleBot("8964935625:AAHU8CHepEwH81iTZsL1qwGjqY8mNvfkuDEKEN
def ai_reply(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content

@bot.message_handler(func=lambda m: True, content_types=['text'])
def handle_message(message):
    bot.reply_to(message, ai_reply(message.text))

@bot.business_message_handler(func=lambda m: True, content_types=['text'])
def handle_business(message):
    bot.reply_to(message, ai_reply(message.text))

bot.polling(allowed_updates=["message", "business_message"])
