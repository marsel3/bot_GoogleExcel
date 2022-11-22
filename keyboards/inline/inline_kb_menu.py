from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db_users


back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back_to_menu')
         ]
    ]
)


"""def catalog_markup():
    m1 = db_tovars.category()
    btns = []
    btns.append([InlineKeyboardButton(text='Поиск товара', callback_data='search')])
    for i in m1:
        btns.append([InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{i[0]}')])
    btns.append([InlineKeyboardButton(text='Назад', callback_data='back_to_menu')])

    return InlineKeyboardMarkup(inline_keyboard=btns)
"""


