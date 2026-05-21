import telebot
from groq import Groq

client = Groq(api_key="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")
bot = telebot.TeleBot("8964935625:AAHU8CHepEwH81iTZsL1qwGjqY8mNvfkuDE")

@bot.message_handler(func=lambda m: True)
def handle(message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.polling()
