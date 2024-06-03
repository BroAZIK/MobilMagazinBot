from telegram import Bot
TOKEN = "6752443146:AAGFpgwjv6P8MZ8NYtNihcQkCo7qxdOdvB0"

bot = Bot(token=TOKEN)

def get_info():
    print(bot.get_webhook_info())


def delete():
    print(bot.delete_webhook())


def set():
    url = 'https://MobilMagazinBot.pythonanywhere.com/webhook'
    print(bot.set_webhook(url=url))

set()
