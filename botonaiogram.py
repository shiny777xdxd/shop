import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.types.message import ContentTypes
import sqlite3
from db import Database
from pyqiwip2p import QiwiP2P
import random
import configur
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# logging.basicConfig(level=logging.INFO)

bot = Bot(token=configur.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
id_adm = "5360547434"

db = Database("database.db")

# p2p = QiwiP2P(auth_key=configur.QIWI_TOK)

#
# def is_number(_str):
#     try:
#         int(_str)
#         return True
#     except ValueError:
#         return False
#

# main = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
# main.add("Каталог").add("Профиль").add("Админ")
#
# privates = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
# privates.add("Помощь").add("Программирование").add("Деанон").add("Схемки")
#
admin = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
admin.add("Добавить товар").add("Удалить товар").add("Рассылка")


oplata = InlineKeyboardMarkup(row_width=2)
oplata.add(InlineKeyboardButton(text="Купить", callback_data="buy"), InlineKeyboardButton(text="Назад", callback_data="back"))








@dp.message_handler(commands=["start"])
async def start(message: types.message):
    user = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("Создать майнер"))
    markup.add(types.KeyboardButton("Помощь"))
    markup.add(types.KeyboardButton("Инструкции", web_app=WebAppInfo(url="https://shiny777xdxd.github.io/sneak.html")))
    await bot.send_message(message.from_user.id, f'❤️‍🔥Привет, {user}❤️‍🔥', reply_markup=markup)
    # if message.chat.type == "private":
    #     if not db.user_exists(message.from_user.id):
    #         db.add_user(message.from_user.id)
    # await bot.send_message(message.from_user.id, f"Добро пожаловать. Ваш счет: {db.user_money(message.from_user.id)} руб", reply_markup=oplata)



@dp.message_handler(text="Помощь")
async def hack(message: types.message):
    markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup1.add(types.KeyboardButton("Создать майнер"))
    markup1.add(types.KeyboardButton("Помощь"))
    markup1.add(types.KeyboardButton("Инструкции", web_app=WebAppInfo(url="https://shiny777xdxd.github.io/sneak.html")))
    await message.answer("Задать вопрос можно администратору: https://t.me/sneak_supprot", reply_markup=markup1)



mark1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

markup777 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
mark = types.KeyboardButton("Выбирайте проценты нагрузки:")
markup777.add(types.KeyboardButton("20%"))
markup777.add(types.KeyboardButton("40%"))
markup777.add(types.KeyboardButton("50%"))
markup777.add(types.KeyboardButton("60%"))
markup777.add(types.KeyboardButton("70%"))
markup777.add(types.KeyboardButton("80%"))
markup777.add(types.KeyboardButton("90%"))
mark1.add(mark, markup777)



@dp.message_handler(text="Создать майнер")
async def adm(message: types.message):

    await message.answer('Укажите максимальную нагрузку на CPU (процессор), когда компьютер используется, от 0 до 100%. (Рекомендуется не более 40%)', reply_markup=mark1)












# @dp.callback_query_handler(lambda c: c.data == 'buy')
# async def process_payment(callback_query: types.CallbackQuery):
#     payment_url = 'https://www.free-kassa.ru/merchant/cash.php?m=YOUR_MERCHANT_ID&id=ORDER_ID&oa=AMOUNT&o=SIGNATURE'
#     await bot.send_message(callback_query.from_user.id, f'Оплатить: [ссылка] ({payment_url})', parse_mode=types.ParseMode.MARKDOWN)
#     await bot.answer_callback_query(callback_query.id)
#
# #
# @dp.callback_query_handler(lambda c: c.data.startswith('freekassa_payment'))
# async def process_payment_result(callback_query: types.CallbackQuery):
#     # Обработайте результат оплаты здесь
#     await bot.send_message(callback_query.from_user.id, 'Спасибо за оплату!')
#


# @dp.callback_query_handler(text="buy")
# async def top_up(callback: types.CallbackQuery):
#     await bot.delete_message(callback.from_user.id, callback.message.message_id)
#     await bot.send_message(callback.from_user.id, "Введите сумму пополнения:")
#
#

# WSA OPLATA QIWI

# def buy_menu(isUrl=True, url="", bill=""):
#     qiwiMenu = InlineKeyboardMarkup(row_width=1)
#     if isUrl:
#         btnURLQIWI = InlineKeyboardButton(text="Ссылка на оплату", url=url)
#         qiwiMenu.insert(btnURLQIWI)
#
#     btnCHECKQIWI = InlineKeyboardButton(text="Проверить оплату", callback_data="check_" + bill)
#     qiwiMenu.insert(btnCHECKQIWI)
#     return qiwiMenu
#
#


#
# @dp.message_handler()
# async def bot_mess(message: types.message):
#     if message.chat.type == "private":
#         if is_number(message.text):
#             message_money = int(message.text)
#             if message_money >= 500:
#                 comment = str(message.from_user.id) + "_" + str(random.randint(1000, 9999))
#                 bill = p2p.bill(amount=message_money, lifetime=15, comment=comment)
#
#                 db.add_check(message.from_user.id, message_money, bill.bill_id)
#
#                 await bot.send_message(message.from_user.id, f"Вам нужно оплатить {message_money} руб \n Ссылка: {bill.pay_url} , обязательно укажите комментарий к оплате {comment}", reply_markup=buy_menu(url=bill.pay_url, bill=bill.bill_id))
#             else:
#                 await bot.send_message(message.from_user.id, "Минимальная сумма пополнения 500 рублей")
#         else:
#             await bot.send_message(message.from_user.id, "Введите целое число")
#
#
#


# @dp.callback_query_handler(text_contains="check_")
# async def check(callback: types.CallbackQuery):
#    bill = str(callback.data[6: ])
#    info = db.get_check(bill)
#    if info != False:
#        if str(p2p.check(bill_id=bill).status) == "PAID":
#            user_money = db.user_money(callback.from_user.id)
#            money = int(info[2])
#            db.set_money(callback.from_user.id, user_money+money)
#            await bot.send_message(callback.from_user.id, "Ваш счет пополнен, напишите /start")
#            db.delete_check(callback.from_user.id)
#        else:
#             await bot.send_message(callback.from_user.id, "Вы не оплатили счет!", reply_markup=buy_menu(False, bill=bill))
#    else:
#        await bot.send_message(callback.from_user.id, "Счет не найден")
#





@dp.message_handler(text="Админ")
async def adm(message: types.message):
    if message.from_user.id == 5360547434:
        await message.answer("Админ панель:", reply_markup=admin)
    else:
        await message.answer("Ты не админ!")




# @dp.message_handler(commands=["pay_hak"])      Оплата платежкой
# async def payhak(message: types.message):
#     await bot.send_invoice(message.chat.id, 'Приватка "Хаккинг"', 'Покупка приватки по хаккингу', 'invoice', configur.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Покупка приватки', 1000 * 100)])
#
#
# @dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
# async def pay(message: types.message):
#     await message.answer(f'Вот ссылка на приватку:')


@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.message):
    await message.answer(message.web_app_data.data)


if __name__ == "__main__":
    executor.start_polling(dp)

