from telegram import InlineKeyboardButton 

start_but = [
    ["Iphone","Redmi","Poco"],
    ["Huawei", "Samsung", "Honor"],
    ["Mening e'lonlarim📣","E'lon joylash ➕📱"],
    ["Bot haqida📊"]
]

admin_start_but = [
    ["Ulanishlar🔗","Base👥📱"],
    ["Telefonlar💯","Uniq id🔍","Tozalash🧹"],
    ["Bot haqida📊"]
]

phones_but = [
    ["Iphone","Redmi","Poco"],
    ["Huawei", "Samsung", "Honor"],
    ["Bot haqida📊"]

]

ortga = [
    ["Ortga🔙"]
]

cleaning = [
    ["Yo'q qilish🔑","Ortga🔙"]
]

inline_channel = [
    [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]
]

inline_celler = [
    [InlineKeyboardButton("Telefon egasi📱👤", url="https://t.me/Mobil_Magazin")]
]  

next_prev_but = [
        [InlineKeyboardButton("⏮", callback_data="prev"), InlineKeyboardButton("⏭", callback_data="next")],
        [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="ADMIN")]
        ]

inline_done = [
    [InlineKeyboardButton("Bekor qilish🚫", callback_data="cancel"), InlineKeyboardButton("Joylash✅", callback_data="done")]
]

inline_my1 = [
    [InlineKeyboardButton("O'chirish🗑", callback_data="delete")],
    [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]
]

inline_my2 = [
    [InlineKeyboardButton("⏮", callback_data="my_prev"), InlineKeyboardButton("O'chirish🗑", callback_data="delete"), InlineKeyboardButton("⏭", callback_data="my_next")],
    [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]
]


inline_all1 = [
    [InlineKeyboardButton("O'chirish🗑", callback_data="delete")],
    [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]
]

inline_all2 = [
    [InlineKeyboardButton("⏮", callback_data="all_prev"), InlineKeyboardButton("O'chirish🗑", callback_data="delete"), InlineKeyboardButton("⏭", callback_data="all_next")],
    [InlineKeyboardButton("MobilMagazin | 🇺🇿", url="https://t.me/Mobil_Magazin")]
]
