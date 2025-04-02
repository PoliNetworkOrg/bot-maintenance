import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set.")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def echo_all(message):
    bot.reply_to(message, "This bot is under maintenance.\nIf you need help with PoliNetwork's materials, contact @toto04_1 or @lorenzocorallo")

bot.infinity_polling()
