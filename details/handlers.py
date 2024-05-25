from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Bot, InputMediaPhoto, InputMediaVideo
from telegram.ext import CallbackContext
from telegram.parsemode import ParseMode
from pprint import pprint
from .messages import *
from .buttons import *
from settings import *
from database.db import *
import json

# bot = Bot(token=TOKEN)

def start(update: Update, context):
    user_id = update.effective_chat.id
    first = update.effective_chat.first_name

    if user_id == ADMIN_ID:
        update.message.reply_photo(
            photo=start_photo,
            caption=admin_start,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True)
        )
    else:  
        update.message.reply_photo(
        photo=start_photo,
        caption=start_mes.format(first),
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True)
        )
    try: 
        insert(table="index",user_id=update.message.chat.id, data={
            "Stage": "start",
            "Iphone": 0,
            "Redmi": 0,
            "Poco": 0,
            "Samsung": 0,
            "Huawei": 0,
            "Honor": 0,
            "My_phones": 0,
            "All": 0
        })
    except:
        upd(table="index",user_id=update.message.chat.id, data={
            "Stage": "start",
            "Iphone": 0,
            "Redmi": 0,
            "Poco": 0,
            "Samsung": 0,
            "Huawei": 0,
            "Honor": 0,
            "My_phones": 0,
            "All": 0
        })
    # bot.edit_message_reply_markup(message_id=update.message.message_id, chat_id=update.message.chat.id, reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))

def add_phone(update: Update, context):
    user_id = update.message.chat.id

    upd(table="index", user_id=user_id, data={"Stage": "add_phone"})
    update.message.reply_photo(
        photo=brend_photo,
        caption=add_phone_mes,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=ReplyKeyboardMarkup(phones_but, resize_keyboard=True)
    )

    # update.message.reply_sticker(sticker=brend_stick)
    # update.message.reply_text(text=add_phone_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(phones_but, resize_keyboard=True))
def back(update: Update, context):
    user_id = update.message.chat.id
    if user_id != ADMIN_ID:
        doccer = get(table="index", user_id=user_id)['edit_doc']
        if doccer != 0:
            delete(product_id=doccer)
            upd(table="index", user_id=user_id, data={"edit_doc": 0})
        upd(table="index", user_id=user_id, data={"Stage": "start"})
        update.message.reply_text(
            text=menu_mes,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True)
        )
    else:
        upd(table="index", user_id=user_id, data={"Stage": "start"})
        update.message.reply_text(text=menu_mes, reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True), parse_mode=ParseMode.MARKDOWN_V2)
import os
def text(update: Update, context):
    user_id = update.message.chat.id
    stage = get(table="index", user_id=user_id)['Stage']
    xabar = update.message.text


    if xabar == get_users_on or xabar == "Base👥📱":
            update.message.reply_document(document=open("database/users.json", "rb"))
            update.message.reply_document(document=open("database/products.json", "rb"))

    if xabar == clear_phones_on or xabar == "Tozalash🧹":
            update.message.reply_text(text="*Telefonlar bazasini tozalamoqchimisiz🆘❓*", reply_markup=ReplyKeyboardMarkup(cleaning, resize_keyboard=True), parse_mode=ParseMode.MARKDOWN_V2)

    if xabar == "Yo'q qilish🔑":
            db2.truncate()
            update.message.reply_text(text="*Barcha telefonlar o'chirib tashlandi *", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True))

    if xabar == "Uniq id🔍":
        upd(table="index", user_id=user_id, data={"Stage": "uniq"})
        update.message.reply_text(
            text="*Siz ko'rmoqchi bo'lgan e'lon uniq id'sini kiriting*🎯",
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True)
        )

    if xabar == "Ulanishlar🔗":
        upd(table="index", user_id=user_id, data={"Stage": "connects"})
        update.message.reply_text(
            text="*Hozircha ushbu bo'lim ishlamaydi*❗️",
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True)
        )


    if xabar == "Telefonlar💯":
        index = get(table="index", user_id=user_id)["All"]
        phones = get(table="phone")
        if index >= len(phones):
            upd(table="index", user_id=user_id, data={"All": 0})
        if len(phones) == 0:
            update.message.reply_text(text=have_not, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=InlineKeyboardMarkup(inline_channel))
            upd(table="index", user_id=user_id, data={"Stage": "start"})
        if len(get(table="phone")) == 1:
            upd(table="index", user_id=user_id, data={"Stage":"All"})
            phone_info = phones[0]
            update.message.reply_photo(
                photo=phone_info['photo_id'],
                reply_markup=InlineKeyboardMarkup(inline_all1),
                caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info["uniq_id"],index+1, len(phones)),
                parse_mode=ParseMode.HTML,

            )
        else:
            phone_info = phones[index]
            update.message.reply_photo(
                photo=phone_info['photo_id'],
                reply_markup=InlineKeyboardMarkup(inline_all2),
                caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],index+1, len(phones)), parse_mode=ParseMode.HTML,

            )

    if stage == "uniq":
        phone = get(uniq_id=xabar)
        if phone != []:
            phone_info = phone[0]
            update.message.reply_photo(
                photo=phone[0]['photo_id'],
                reply_markup=InlineKeyboardMarkup(inline_all1),
                caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info["uniq_id"], 1, 1),
                parse_mode=ParseMode.HTML,

            )
            
        else:
            update.message.reply_text(
                text="*Siz kiritgan uniq id xato bo'lishi mumkin*❗️",
                parse_mode=ParseMode.MARKDOWN_V2
            )
        
        update.message.reply_text(
            text="*Siz asosiy menyudasiz👇🏻*",
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True)
        )
        upd(table="index", user_id=user_id, data={"Stage": "start"})

    if stage == "start" or stage == "My_phones" or stage == "Iphone" or stage == "Redmi" or stage == "Poco" or stage == "Huawei" or stage == "Samsung" or stage == "Honor":
        if xabar == "Iphone" or xabar == "Redmi" or xabar == "Poco" or xabar == "Huawei" or xabar == "Honor" or "Samsung":
            
            index = get(table="index", user_id=user_id)[xabar]
            phones = get(table="phone", product_type=xabar)
            if index >= len(phones):
                upd(table="index", user_id=user_id, data={xabar: 0})
            index = get(table="index", user_id=user_id)[xabar]
            try:

                upd(table="index", user_id=user_id, data={"Stage": xabar})
                phone_info = phones[index]
                keyboard=[[InlineKeyboardButton("⏮", callback_data="prev"),InlineKeyboardButton("Batafsil📱", url=f"tg://user?id={phone_info['user_id']}"), InlineKeyboardButton("⏭", callback_data="next")],
                          [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]]
                          
                update.message.reply_photo(
                    photo=phone_info['photo_id'],
                    caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'], phone_info['uniq_id'], index+1, len(phones)),
                    parse_mode=ParseMode.HTML,
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
        
            except:
                update.message.reply_text(
                    text=not_enough_phone.format(xabar),
                    parse_mode=ParseMode.MARKDOWN_V2,
                    reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True)
                )


    if stage == "add_phone":
        if xabar == "Iphone" or xabar == "Redmi" or xabar == "Poco" or xabar == "Huawei" or xabar == "Samsung" or xabar == "Honor":
            upd(table="index", user_id=user_id, data={"Stage": xabar})
            # update.message.reply_photo(
            #     photo=rasm_photo,
            #     caption=get_photo_mes,
            #     parse_mode=ParseMode.MARKDOWN_V2,
            #     reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True)
            # )

            update.message.reply_sticker(sticker=rasm_stick)
            update.message.reply_text(text=get_photo_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))

            # update.message.delete()
            # bot.send_photo(chat_id=update.message.chat_id, photo=rasm_photo, caption=get_photo_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
            try: 
                insert(table="index", user_id=user_id, data={"edit_doc": 0})
                print("yangi edit id belgilandi")
            except:
                upd(table="index", user_id=user_id, data={"edit_doc": 0})
                print("yangi edit id yangilandi")
        else:
            update.message.reply_text(text=error_stage.format(update.message.chat.first_name), parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
    if stage == "get_model":
        upd(table="phone", user_id=user_id, data={"model": xabar})
        upd(table="index", user_id=user_id, data={"Stage": "get_storage"})

        update.message.reply_sticker(sticker=xotira_stick)
        update.message.reply_text(text=get_storage_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        # update.message.reply_photo(photo=xotira_photo,caption=get_storage_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
    if stage == "get_storage":
        upd(table="index", user_id=user_id, data={"Stage": "get_battery"})
        upd(table="phone", user_id=user_id, data={"storage": xabar})

        update.message.reply_sticker(sticker=batareyka_stick)
        update.message.reply_text(text=get_battery_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        # update.message.reply_photo(photo=batareyka_photo,caption=get_battery_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga,resize_keyboard=True))
    if stage == "get_battery":
        upd(table="index", user_id=user_id, data={"Stage": "get_holat"})
        upd(table="phone", user_id=user_id, data={"battery": xabar})

        update.message.reply_sticker(sticker=holat_stick)
        update.message.reply_text(text=get_holat_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        # update.message.reply_text(text=get_holat_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga,resize_keyboard=True))
    if stage == "get_holat":
        upd(table="index", user_id=user_id, data={"Stage": "get_document"})
        upd(table="phone", user_id=user_id, data={"holat": xabar})

        update.message.reply_sticker(sticker=huJJat_stick)
        update.message.reply_text(text=get_document_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        # update.message.reply_text(text=get_document_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
    if stage == "get_document":
        upd(table="index", user_id=user_id, data={"Stage": "get_info"})
        upd(table="phone", user_id=user_id, data={"document": xabar})

        update.message.reply_sticker(sticker=info_stick)
        update.message.reply_text(text=get_info_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        # update.message.reply_text(text=get_info_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
    if stage == "get_info":
        upd(table="index", user_id=user_id, data={"Stage": "get_price"})
        upd(table="phone", user_id=user_id, data={"info": xabar})

        update.message.reply_sticker(sticker=narxi_stick)
        update.message.reply_text(text=get_price_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        # update.message.reply_text(text=get_price_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
    if stage == "get_price":
        upd(table="index", user_id=user_id, data={"Stage": "get_price"})
        upd(table="phone", user_id=user_id, data={"price": xabar, "uniq_id": update.message.message_id})

        phone_info = get(table="phone", user_id=user_id)[-1]  
        pprint(phone_info)
        update.message.reply_photo(photo=phone_info['photo_id'],
                                   caption=get_done_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info']),
                                   parse_mode=ParseMode.HTML,
                                   reply_markup=InlineKeyboardMarkup(inline_done))

def photo(update: Update, context):
    user_id = update.message.chat.id
    data = update.to_dict()
    xabar = get(table="index", user_id=user_id)['Stage']

    if xabar == "Iphone" or xabar == "Redmi" or xabar == "Poco" or xabar == "Huawei" or xabar == "Samsung" or xabar == "Honor":
        doc_ider = insert(table="phone", user_id=user_id, data={"product_type": xabar,"photo_id": data['message']['photo'][-1]['file_id'], "user_id": user_id})
        upd(table="index", user_id=user_id, data={"Stage": "get_model", "edit_doc": doc_ider})
        # update.message.reply_photo(
        #     photo=model_photo,
        #     caption=get_model_mes.format(xabar),  
        #     parse_mode=ParseMode.MARKDOWN_V2,
        #     reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
        update.message.reply_sticker(sticker=model_stick)
        update.message.reply_text(text=get_model_mes.format(xabar), parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(ortga, resize_keyboard=True))
    else:
        update.message.reply_text(
            text=f"{update['message']['photo'][-1]['file_id']}",
            # parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))

def button_callback(update: Update, context):
    query = update.callback_query
    user_id = query.from_user.id
    pprint(query.to_dict())
    stage = get(table="index", user_id=user_id)["Stage"]

    
    if query.data == "done":
        phone = get(table="phone", user_id=user_id)
        print("CALLLBACK KELDI")
        if len(phone) == 1:
            print("BITTA EKAN")
            phone_info = phone[0]
            keyboard = [[InlineKeyboardButton("Telefon egasi | 👤", url=f"tg://user?id={user_id}")]]
            context.bot.send_photo(chat_id=CHANNEL, photo=phone[0]['photo_id'],parse_mode=ParseMode.HTML,caption=post_channel_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info']),
                           reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            phone_info = phone[-1]
            print("KO'P EKAN")
            keyboard = [[InlineKeyboardButton("Telefon egasi | 👤", url=f"tg://user?id={user_id}")]]
            context.bot.send_photo(chat_id=CHANNEL,parse_mode=ParseMode.HTML, photo=phone_info['photo_id'], caption=post_channel_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info']),
                           reply_markup=InlineKeyboardMarkup(keyboard))
        query.delete_message()
        upd(table="index", user_id=user_id, data={"Stage": "start"})
        context.bot.send_photo(chat_id=user_id,caption=done_mes,parse_mode=ParseMode.HTML,photo=done_photo, reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))
        # context.bot.send_text(chat_id=user_id,text=done_mes, reply_markup=InlineKeyboardMarkup(inline_channel))
        
    if query.data == "cancel":
        phone = get(table="phone", user_id=user_id)
        new_media=InputMediaPhoto(media=start_photo, caption=menu_mes, parse_mode=ParseMode.MARKDOWN_V2)
        att = get(table="index", user_id=user_id)['edit_doc']
        delete(product_id=att)
        
        # query.edit_message_media(media=new_media)
        # query.edit_message_reply_markup(reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))
        # query.message.reply_photo(photo="AgACAgQAAxkDAAICAmYcDwq95CKTLxHoTn3jaUTGTYeSAAJ8szEbzZnkULjNacppW6UdAQADAgADcwADNAQ", caption="This is the updated message")
        upd(table="index", user_id=user_id, data={"edit_doc": 0})
        upd(table="index", user_id=user_id, data={"Stage": "start"})

        context.bot.send_photo(chat_id=user_id,photo=start_photo, caption=menu_mes, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))
        query.message.delete()

    if query.data == "delete":
        caption = query.message.caption
        text = caption.split("•┈┈┈•")[1]
        print(text)
        delete(uniq_id=text)
        index = get(table="index", user_id=user_id)[stage]
        upd(table="index", user_id=user_id, data={stage: index-1})
        phones = get(table="phone", user_id=user_id)
        if len(phones) == 0:
            if user_id != ADMIN_ID:
                context.bot.send_message(chat_id=user_id,text=have_not, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))
                query.message.delete()
                upd(table="index", user_id=user_id, data={stage: 0})
            else:
                context.bot.send_message(chat_id=user_id,text=admin_have_not, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True))
                query.message.delete()

        if len(phones) == 1:
            query.message.delete()
            phone_info = phones[0]
            context.bot.send_photo(photo=phones[0]['photo_id'],
                                   chat_id=user_id,
            reply_markup=InlineKeyboardMarkup(inline_my1),
            caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info["uniq_id"],index, len(phones)), parse_mode=ParseMode.HTML)
        else:
            query.message.delete()
            phone_info = phones[index-1]
            print(phone_info)
            
            context.bot.send_photo(
            chat_id=user_id,
            photo=phone_info['photo_id'],
            caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],index, len(phones)), parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(inline_my2))
    if query.data == "next":
        index = get(table="index", user_id=user_id)[stage]
        phones = get(table="phone", product_type=stage)
        
        if index >= len(phones)-1:
            upd(table="index", user_id=user_id, data={stage: 0})
        else:
            upd(table="index", user_id=user_id, data={stage: index+1})
        
        new_index = get(table="index", user_id=user_id)[stage]  
        phone_info = phones[new_index]
        keyboard=[[InlineKeyboardButton("⏮", callback_data="prev"),InlineKeyboardButton("Batafsil📱", url=f"tg://user?id={phone_info['user_id']}"), InlineKeyboardButton("⏭", callback_data="next")],
                          [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]]
        new_media = InputMediaPhoto(media=phone_info['photo_id'], caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],new_index+1, len(phones)), parse_mode=ParseMode.HTML)
        query.edit_message_media(media=new_media)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))

    if query.data == "prev":
        index = get(table="index", user_id=user_id)[stage]
        phones = get(table="phone", product_type=stage)
        
        if index <= 0:
            upd(table="index", user_id=user_id, data={stage: len(phones)-1})
        else:
            upd(table="index", user_id=user_id, data={stage: index-1})
        
        new_index = get(table="index", user_id=user_id)[stage]
        phone_info = phones[new_index]
        keyboard=[[InlineKeyboardButton("⏮", callback_data="prev"),InlineKeyboardButton("Batafsil📱", url=f"tg://user?id={phone_info['user_id']}"), InlineKeyboardButton("⏭", callback_data="next")],
                          [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]]
        new_media = InputMediaPhoto(media=phone_info['photo_id'], caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],new_index+1, len(phones)), parse_mode=ParseMode.HTML)
        query.edit_message_media(media=new_media)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))



    if query.data == "my_next":
        index = get(table="index", user_id=user_id)["My_phones"]
        phones = get(table="phone", user_id=user_id)
        if index >= len(phones)-1:
            upd(table="index", user_id=user_id, data={"My_phones": 0})
        else:
            upd(table="index", user_id=user_id, data={"My_phones": index+1})
        new_index = get(table="index", user_id=user_id)["My_phones"]
        print(new_index)

        
        phone_info = get(table="phone", user_id=user_id)[new_index]
        new_media = InputMediaPhoto(media=phone_info['photo_id'], caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],new_index+1, len(phones)), parse_mode=ParseMode.HTML)

        query.edit_message_media(media=new_media)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(inline_my2))
    if query.data == "my_prev":
        index = get(table="index", user_id=user_id)["My_phones"]
        phones = get(table="phone", user_id=user_id)
        if index <= 0:
            upd(table="index", user_id=user_id, data={"My_phones": len(phones)-1})
        else:
            upd(table="index", user_id=user_id, data={"My_phones": index-1})
        new_index = get(table="index", user_id=user_id)["My_phones"]
        print(new_index)

        
        phone_info = get(table="phone", user_id=user_id)[new_index]
        new_media = InputMediaPhoto(media=phone_info['photo_id'], caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],new_index+1, len(phones)), parse_mode=ParseMode.HTML)

        query.edit_message_media(media=new_media)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(inline_my2))


    if query.data == "all_next":
        index = get(table="index", user_id=user_id)["All"]
        phones = get(table="phone")
        pprint(phones)
        print(f"tellar: {len(phones)}, index: {index}")
        if index >= len(phones)-1:
            upd(table="index", user_id=user_id, data={"All": 0})
        else:
            upd(table="index", user_id=user_id, data={"All": index+1})
        new_index = get(table="index", user_id=user_id)["All"]
        print(new_index)

        
        phone_info = get(table="phone")[new_index]
        new_media = InputMediaPhoto(media=phone_info['photo_id'], caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],new_index+1, len(phones)), parse_mode=ParseMode.HTML)

        query.edit_message_media(media=new_media)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(inline_all2))
    if query.data == "all_prev":
        index = get(table="index", user_id=user_id)["All"]
        phones = get(table="phone")
        if index <= 0:
            upd(table="index", user_id=user_id, data={"All": len(phones)-1})
        else:
            upd(table="index", user_id=user_id, data={"All": index-1})
        new_index = get(table="index", user_id=user_id)["All"]
        print(new_index)

        
        phone_info = get(table="phone")[new_index]
        new_media = InputMediaPhoto(media=phone_info['photo_id'], caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],new_index+1, len(phones)), parse_mode=ParseMode.HTML)

        query.edit_message_media(media=new_media)
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(inline_all2))
def my_phones(update: Update, context):
    user_id = update.message.chat.id
    upd(table="index", user_id=user_id, data={"Stage": "My_phones"})
    index = get(table="index", user_id=user_id)['My_phones']
    phones = get(table="phone", user_id=user_id)
    if index >= len(phones):
        upd(table="index", user_id=user_id, data={"My_phones": 0})
    index = get(table="index", user_id=user_id)['My_phones']

    if len(phones) == 0:
        # phone_info = phones[0]
        update.message.reply_text(text=have_not, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=InlineKeyboardMarkup(inline_channel))
        upd(table="index", user_id=user_id, data={"Stage": "start"})
    if len(phones) == 1: 
        phone_info = phones[0]
        update.message.reply_photo(photo=phones[0]['photo_id'],
        reply_markup=InlineKeyboardMarkup(inline_my1),
        caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info["uniq_id"],index+1, len(phones)), parse_mode=ParseMode.HTML)
    else:
        phone_info = phones[index]
        update.message.reply_photo(
            photo=phone_info['photo_id'],
            caption=my_phones_mes.format(phone_info['product_type'], phone_info['model'], phone_info['storage'], phone_info['holat'], phone_info['battery'], phone_info['document'], phone_info['price'], phone_info['info'],phone_info['uniq_id'],index+1, len(phones)), parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(inline_my2))
def sticker(update: Update, context):
    user_id = update.message.chat.id
    file_id = update.message.sticker.file_id
    update.message.reply_text(text=file_id)

def stats(update, context):
    users = len(db1.table("Index"))
    phones = len(db2)
    upd(table="index",user_id=update.message.chat.id, data={"Stage": "start"})
    if ADMIN_ID == update.message.chat.id:
        update.message.reply_text(text=stats_mes.format(users, phones), parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True))
    else:
        update.message.reply_text(text=stats_mes.format(users, phones), parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardMarkup(start_but, resize_keyboard=True))
