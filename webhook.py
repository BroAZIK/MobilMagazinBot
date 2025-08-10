from telegram import Bot
TOKEN = "6752443146:AAGspa3xdNRxnJ0wIT4EAkOt3mozgzWQi7U"

bot = Bot(token=TOKEN)

def get_info():
    print(bot.get_webhook_info())


def delete():
    print(bot.delete_webhook())


def set():
    url = 'https://MobilMagazinBot.pythonanywhere.com/webhook'
    print(bot.set_webhook(url=url))

set()
