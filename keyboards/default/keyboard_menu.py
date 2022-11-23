from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='🗂️ Посмотреть цены'),
                KeyboardButton(text='🗂️ Записаться'),
            ],
            [
                KeyboardButton(text='📲️ Связаться со мной'),
            ],
        ],
    resize_keyboard=True
)