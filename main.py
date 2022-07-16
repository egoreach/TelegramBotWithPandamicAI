# -*- coding: utf-8 -*-

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import asyncio
import logging

import markup as nav
import readtxt as rt
import pars as ps
import config

from ai import get_city_prediction


bot = Bot(token=config.token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}!'.format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Информация о COVID-19":
        await bot.send_message(message.from_user.id, "Информация о COVID-19", reply_markup=nav.otherMenu2)
    elif message.text == "Сколько людей заражено за сегодня":
        await bot.send_message(message.from_user.id, f'Сегодня заразились {ps.parser()} человек.')
    elif message.text == "Узнать прогноз":
        await bot.send_message(message.from_user.id, "Какой город вас интересует?")
    elif message.text == "Интересное о COVID-19":
        await bot.send_message(message.from_user.id, "Интересное о COVID-19", reply_markup=nav.otherMenu)
    elif message.text == "Факты о COVID-19":
        await bot.send_message(message.from_user.id, rt.arbitrary())
    elif message.text == "Назад":
        await bot.send_message(message.from_user.id, "Интересное о COVID-19", reply_markup=nav.mainMenu)
    elif message.text == "Профилактика COVID-19":
        await bot.send_message(message.from_user.id, "Профилактика COVID-19", reply_markup=nav.preventionMenu)
    elif message.text == "Симптомы":
        await message.answer("1. Высокая температура.\n\n2. Затрудненное дыхание.\n\n3. Чихание, кашель и заложенность носа.\n\n4. Боли в мышцах и в груди.\n\n5. Головная боль и слабость.\n\n6. Возможна тошнота, рвота и диарея.")
    elif message.text == "Профилактика":
        await message.answer("Всегда мойте руки: когда приходите на работу или возвращаетесь домой. Для профилактики также подойдут влажные салфетки или дезинфицирующие растворы.\n\nИзбегайте ненужных поездок и не ходите в места массового скопления людей.\n\nНе подносите руки к носу и глазам. Быстрее всего вирус попадает в организм через слизистую оболочку. Когда чихаете всегда прикрывайтесь платком.\n\nНа время, пока разные страны мира борются с коронавирусом, не следует путешествовать заграницу. В особенности туда, где ситуация с коронавирусом крайне тяжелая.\n\nВакцинируйтесь. Вакцина – единственное надежное средство профилактики вируса. Только пройдя вакцинацию мы сможем остановить передачу вируса и защитить себя от его тяжелых последствий.")
    else:
        try:
            prediction, real, miss = get_city_prediction(message.text)
            await message.reply(f"{prediction} - предсказание нашей модели машинного обучения. \n"
                                 f"{real} - показатель из размеченных профессионалами данных. \n"
                                 f"Погрешность составила {miss}.")
        except:
            await message.reply("Такого города нет в нашей базе.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
