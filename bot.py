import telebot
from groq import Groq

GROQ_KEY = "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"
TG_TOKEN = "8964935625:AAHU8CHepEwH81iTZsL1qwGjqY8mNvfkuDE"

client = Groq(api_key=GROQ_KEY)
bot = telebot.TeleBot(TG_TOKEN)

def ai(text):
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": text}]
    )
    return r.choices[0].message.content

@bot.message_handler(func=lambda m: True)
def msg(m):
    bot.reply_to(m, ai(m.text))

@bot.business_message_handler(func=lambda m: True)
def biz(m):
    bot.send_message(m.chat.id, ai(m.text),
    business_connection_id=m.business_connection_id)

bot.infinity_polling(allowed_updates=
["message","business_message"])
