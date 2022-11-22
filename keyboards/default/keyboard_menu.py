from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='🗂️ Записаться'),
            ],
            [
                KeyboardButton(text='👤 Профиль'),
            ],
        ],
    resize_keyboard=True
)