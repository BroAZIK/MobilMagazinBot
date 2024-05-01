import requests
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from settings import *
from details.handlers import *

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def register_handlers():

    dispatcher.add_handler(CommandHandler("start", start)),
    dispatcher.add_handler(MessageHandler(Filters.text("Ortga🔙"), back)),
    dispatcher.add_handler(CallbackQueryHandler(button_callback)),
    dispatcher.add_handler(MessageHandler(Filters.text("E'lon joylash ➕📱"), add_phone)),
    dispatcher.add_handler(MessageHandler(Filters.text("Mening e'lonlarim📣"), my_phones)),
    dispatcher.add_handler(MessageHandler(Filters.text("Bot haqida📊"), stats)),
    dispatcher.add_handler(MessageHandler(Filters.text, text)),
    dispatcher.add_handler(MessageHandler(Filters.photo, photo)),
    dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))

    updater.start_polling()
    updater.idle()
register_handlers()
