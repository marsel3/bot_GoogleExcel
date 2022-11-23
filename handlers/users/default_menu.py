from aiogram import types
from loader import dp, db_users
from keyboards.inline import inline_kb_menu


@dp.message_handler(text=['🗂️ Посмотреть цены'])
async def show_catalog(message: types.Message):
    #await message.delete()
    await message.answer(f'Вы перешли в каталог, выберите категорию нужного вам товара.',
                         reply_markup=inline_kb_menu.catalog_markup())

@dp.message_handler(text=['🗂️ Записаться'])
async def show_basket(message: types.Message):
    # await message.delete()
    markup, string = inline_kb_menu.basket_markup(message.from_user.id)
    await message.answer(string, reply_markup=markup)



@dp.message_handler(text=['📲📲️ Связаться со мной'])
async def show_contact(message: types.Message):
    # await message.delete()
    await dp.bot.send_location(message.chat.id,
                               latitude=55.78556,
                               longitude=49.12472)
    await message.answer(f'SHOPBOT - удобный телеграмм магазин'
                         f'\n\n📲️ Telegram: @marssak'
                         f'\n\nℹ️г. Казань, метро Площадь Габдуллы Тукая',
                               reply_markup=inline_kb_menu.back_to_menu)
"""    await message.answer(f'Иногда лучшая помощь человеку - это просто не мешать. ☝️',
                         reply_markup=inline_kb_menu.back_to_menu)"""
