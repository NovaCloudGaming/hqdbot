#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pyqiwip2p import QiwiP2P
from pyqiwip2p.types import QiwiCustomer, QiwiDatetime
import sqlite3
import requests
import asyncio
import menu
import settings
import functions as func
import telebot
from telebot import types
import time
import datetime
import random
QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InI1c25uMy0wMCIsInVzZXJfaWQiOiI3OTM3Nzg3OTA3MCIsInNlY3JldCI6ImVlNjcyYjQzNTljOGJiZjhjMWEwNGQwN2Y5M2M1YzUyNThmYjI2ZGMyYWRiNTY1MzNhMDZhMzhiYTAzNTRlNWYifX0="
p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

TO_CHAT_ID =  717827324
def start_bot():
    bot = telebot.TeleBot(settings.bot_token)

    # Command start
    @bot.message_handler(commands=['start'])
    def handler_start(message):
        chat_id = message.chat.id
        func.first_join(user_id=chat_id, name=message.from_user.username, code=message.text[6:])
        bot.send_message(chat_id,
                         '👋 Привет {}! 👋\n🏪 Добро пожаловать в наш магазин! 🏪\n👇 Нажми на одну из кнопок снизу 👇 '.format(message.from_user.first_name),
                         reply_markup=menu.main_menu)



    # Обработка данных
    @bot.callback_query_handler(func=lambda call: True)
    def handler_call(call):
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        if call.data == 'replenish_balance1':
            bot.send_message(
                chat_id=TO_CHAT_ID,
                text='Кто-то нажал на кнопку поплнить баланс',
                )

        if call.data == 'oplatil1':
            bot.send_message(
                chat_id=TO_CHAT_ID,
                text='Кто-то нажал на кнопку Я оплатил',
                )

        if call.data == '1010':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/6368.jpg','rb'), caption= 'Цена: 450рублей' )
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '999':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/6675.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '888':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/7150.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)


        if call.data == '777':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/5528.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '666':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/5153.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '555':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/5983.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '444':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/6956.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '333':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/8394.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '222':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/5534.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == '111':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id,
                           photo=open('photo/4884.jpg','rb'), caption= 'Цена: 450рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇👇',
                reply_markup=menu.korz5)

        if call.data == 'jij':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo=open('photo/359d8bb9-vaporesso-osmall-pod-kit-350mah_006856dd4ce7-768x768.jpg', 'rb'),                    )
            bot.send_message(
                chat_id=chat_id,
                text='Выбирите подходящий товар👇',
                reply_markup=menu.jij1)

        if call.data == 'fi1':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Цена: 800рублей',
                reply_markup=menu.korz4)

        if call.data == 'vap':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo=open('photo/359d8bb9-vaporesso-osmall-pod-kit-350mah_006856dd4ce7-768x768.jpg', 'rb'),                    )
            bot.send_message(
                chat_id=chat_id,
                text='Выбирите подходящий товар👇',
                reply_markup=menu.vap1 )

        if call.data == 'fi':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Цена: 1800рублей',
                reply_markup=menu.korz3)

        if call.data == 'voop':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo=open('photo/4.png', 'rb'), )
            bot.send_message(
                chat_id=chat_id,
                text='Выбирите подходящий товар👇',
                reply_markup=menu.voop1
            )

        if call.data == 'sil':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/juul-RU-devicekit-front-silver-V01 (1).png', 'rb'), caption='Цена: 650рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz2)

        if call.data == 'rub':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/nabor-juul-labs-juul-8w-200-mah.jpg', 'rb'), caption='Цена: 650рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz2)

        if call.data == 'sl':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/juul-RU-devicekit-front-silver-V01.jpg', 'rb'), caption='Цена: 650рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz2)

        if call.data == 'jul':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выбирите подходящий товар👇',
                reply_markup=menu.jul1
            )

        if call.data == 'oreh':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/e1df079c48835dca1ca438bddbd68ecf.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'mint':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/nabor-nerazbornyj-hqd-280-mah.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'cola':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/_.png', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'Cin':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/6018837362.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)


        if call.data == 'lim':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/hqd-cuvie-cheesecake-lemon-pie-650x650.png', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)


        if call.data == 'ananas':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/ananas-1600x1600.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)


        if call.data == 'mult':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/hqd-mixed-fruit-vape--400x400.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'din':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/6018116771.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'apel':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/09fe4101d37667cb907e3e9c54cc133d.png', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'lich':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/91fd94006f3211eabe83d4d2528df4fe_aeb3d3b7846911eabe8ad4d2528df4fe.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)


        if call.data == 'man':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/f49583ddf7815d19853d681afae08dc6.png', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'apple':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/f6bb2922c2140c6f24cb3210e6055bdb.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'vin':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/f6e6d6c28f7ee0e0b34c03cfbe14a0da.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)


        if call.data == 'pers':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/d0fb478cff0f11ea9190fa163e716807_d10e6984ff0f11ea9190fa163e716807.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'ban':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/odnorazovaya-sigareta-hqd-cuvie-banana-ice.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'vish':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/hqd_v2_disposable_pod_cherry_50mg_1sht.png', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'bl':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/blueberry_.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)

        if call.data == 'klub':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_photo(chat_id=chat_id, photo = open('photo/strawberry_.jpg', 'rb'), caption='Цена: 250рублей')
            bot.send_message(
                chat_id=chat_id,
                text='👇👇👇👇',
                reply_markup=menu.korz)





        if call.data == 'hqd1':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выбирите подходящий товар👇',
                reply_markup = menu.hqd2
            )

        if call.data == 'catalog1':
            bot.send_message(
                chat_id=chat_id,
                text='Выбирите подходящий товар👇',
                reply_markup = menu.catalog2

            )


        if call.data == 'replenish_balance1':
            bot.send_message(
                chat_id=chat_id,
                text='Выберите сумму пополнения',
                reply_markup = menu.oplata

            )

        if call.data == '100':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            sto = random.randint(111111111,999999999)
            new_bill = p2p.bill(bill_id=sto, amount=100, lifetime=45)
            bot.send_message(
                chat_id=chat_id,
                text='Для оплаты перейдите по указанной ссылке:'+
                new_bill.pay_url +'''

            💸 Стоимость Вашего пополнения составляет 100 ₽!
            💾 Обязательно оплатите заказ в течение срока действия ссылки!
            После оплаты нажмите кнопку "✅ Я оплатил"👇''',
                reply_markup=menu.oplatil
            )

        if call.data == '300':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            tri = random.randint(111111111, 999999999)
            new_bill = p2p.bill(bill_id=tri, amount=300, lifetime=45)
            bot.send_message(
                chat_id=chat_id,
                text='Для оплаты перейдите по указанной ссылке:'+
                new_bill.pay_url +'''

            💸 Стоимость Вашего пополнения составляет 300 ₽!
            💾 Обязательно оплатите заказ в течение срока действия ссылки!
            После оплаты нажмите кнопку "✅ Я оплатил"👇''',
                reply_markup=menu.oplatil
            )
        if call.data == '500':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            pat = random.randint(111111111, 999999999)
            new_bill = p2p.bill(bill_id=pat, amount=500, lifetime=45)
            bot.send_message(
                chat_id=chat_id,
                text='Для оплаты перейдите по указанной ссылке:'+
                new_bill.pay_url +'''

            💸 Стоимость Вашего пополнения составляет 500 ₽!
            💾 Обязательно оплатите заказ в течение срока действия ссылки!
            После оплаты нажмите кнопку "✅ Я оплатил"👇''',
                reply_markup=menu.oplatil
            )
        if call.data == '1000':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            tis = random.randint(111111111, 999999999)
            new_bill = p2p.bill(bill_id=tis, amount=1000, lifetime=45)
            bot.send_message(
                chat_id=chat_id,
                text='Для оплаты перейдите по указанной ссылке:'+
                new_bill.pay_url +'''

            💸 Стоимость Вашего пополнения составляет 1000 ₽!
            💾 Обязательно оплатите заказ в течение срока действия ссылки!
            После оплаты нажмите кнопку "✅ Я оплатил"👇''',
                reply_markup=menu.oplatil
            )








        # Main menu
        if call.data == 'catalog':
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text='Каталог',
                reply_markup=func.menu_catalog()
            )

        if call.data == 'exit_from_catalog':
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text='Вы вернулись назад',
                reply_markup=menu.main_menu
            )


        if call.data in func.list_sections():
            name = call.data
            product = func.Product(chat_id)
            product_dict[call.message.chat.id] = product
            product.section = name

            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text='❕ Выберите нужный товар',
                reply_markup=func.menu_section(call.data)
            )



        if call.data == 'buy':
            try:
                product = product_dict[chat_id]
                msg = bot.send_message(chat_id=chat_id,
                                       text=f'❕ Введите кол-во товара\n❕ От 1 - {product.amount_MAX}')
                bot.register_next_step_handler(msg, buy)
            except:
                pass
                
        if call.data == 'info':
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=settings.info,
                reply_markup=menu.main_menu
            )

        if call.data == 'purchases':
            msg = func.basket(chat_id)
            if len(msg) > 0:
                bot.edit_message_text(chat_id=chat_id,
                                      message_id=message_id,
                                      text=msg,
                                      reply_markup=menu.main_menu)
            if len(msg) == 0:
                bot.edit_message_text(chat_id=chat_id,
                                      message_id=message_id,
                                      text='Твоя корзина пуста!',
                                      reply_markup=menu.main_menu)


        if call.data == 'exit_to_menu':
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text='Вы вернулись в главное меню',
                reply_markup=menu.main_menu
            )

        if call.data == 'btn_ok':
            bot.delete_message(chat_id, message_id)

        if call.data == 'profile':
            info = func.profile(chat_id)
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=settings.profile.format(
                                      id=info[0],
                                      login=f'@{info[1]}',
                                      data=info[2][:19],
                                      balance=info[5]
                                  ),
                                  reply_markup=menu.main_menu)



        if call.data == 'check_payment':
            check = func.check_payment(chat_id)
            if check[0] == 1:
                bot.edit_message_text(chat_id=chat_id,
                                      message_id=message_id,
                                      text=f'✅ Оплата прошла\nСумма - {check[1]} руб',
                                      reply_markup=menu.main_menu)

                bot.send_message(chat_id=settings.admin_id,
                                 text='💰 Пополнение баланса\n'
                                      f'🔥 От - {chat_id}\n'
                                      f'🔥 Сумма - {check[1]} руб')
        if call.data == 'back7':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выберите подходящий товар👇',
                reply_markup=menu.jij1
           )

        if call.data == 'back6':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выберите подходящий товар👇',
                reply_markup=menu.vap1
           )

        if call.data == 'back5':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выберите подходящий товар👇',
                reply_markup=menu.voop1
           )

        if call.data == 'back4':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выберите подходящий товар👇',
                reply_markup=menu.jul1
           )

        if call.data == 'back3':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выберите подходящий товар👇',
                reply_markup=menu.hqd2
           )

        if call.data == 'back2':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='Выберите подходящий товар👇',
                reply_markup=menu.catalog2
           )

        if call.data == 'back':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)

        if call.data == 'to_close':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)

        if call.data == 'oplatil1':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)
            bot.send_message(
                chat_id=chat_id,
                text='🚫Cрок действия ссылки истёк либо же вы не оплатили товар',
                reply_markup = menu.to_close


            )
        if call.data == 'korz1':
            bot.delete_message(chat_id=chat_id,
                               message_id=message_id)

            bot.send_message(
                chat_id=chat_id,
                text='🚫Ошибка🚫\nДля добавления товаров в корзину на вашем балансе должна быть сумма достаточная для оплаты выбранного товара',
                reply_markup=menu.main_menu

            )


    bot.polling(none_stop=True)



start_bot()
