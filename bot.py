import telebot
from datetime import datetime

# این خط رو حتماً تغییر بده ↓↓↓
BOT_TOKEN = '8548549388:AAGekRcq9wU89End0cQEgSiqDWhhVpCK6pg'   # توکن واقعی رو اینجا بگذار

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من بات نمونه کارم 😊\n"
                          "دستورات:\n"
                          "/time → زمان فعلی\n"
                          "/echo سلام → تکرار می‌کنم چی گفتی")

@bot.message_handler(commands=['time'])
def send_time(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, f"زمان الان: {now}")

@bot.message_handler(commands=['echo'])
def echo_message(message):
    text = message.text[6:].strip()  # متن بعد از /echo
    if text:
        bot.reply_to(message, f"تو گفتی: {text}")
    else:
        bot.reply_to(message, "بعد /echo یه چیزی بنویس!")

print("بات داره اجرا میشه ...")
bot.infinity_polling()