from filters import IsAdmin
from aiogram import types

from loader import dp, db_users

from aiogram.types import CallbackQuery
from keyboards.inline import inline_kb_menu



@dp.message_handler(IsAdmin(), text='/admin')
async def admin(messsage: types.Message):
    await messsage.answer(f'Здравствуйте, {messsage.from_user.full_name},  вы попали в админ панель!')
