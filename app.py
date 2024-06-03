import requests
from flask import Flask, request
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    Dispatcher
)
from settings import *
from details.handlers import *

bot = Bot(token=TOKEN, use_context=True)
dispatcher = Dispatcher(bot, None, workers=0)
app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def register_handlers():

    if request.method == 'GET':
        return "webhook is running...!"
    
    if request.method == 'POST':

        print("Post keldi")
        body = request.get_json()
        
        update = Update.de_json(body, bot)
        dispatcher.add_handler(CommandHandler("start", start)),
        dispatcher.add_handler(MessageHandler(Filters.text("Ortga🔙"), back)),
        dispatcher.add_handler(CallbackQueryHandler(button_callback)),
        dispatcher.add_handler(MessageHandler(Filters.text("E'lon joylash ➕📱"), add_phone)),
        dispatcher.add_handler(MessageHandler(Filters.text("Mening e'lonlarim📣"), my_phones)),
        dispatcher.add_handler(MessageHandler(Filters.text("Bot haqida📊"), stats)),
        dispatcher.add_handler(MessageHandler(Filters.text, text)),
        dispatcher.add_handler(MessageHandler(Filters.photo, photo)),
        dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))

        dispatcher.process_update(update)

        return {'message': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)
