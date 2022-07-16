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
    elif message.text == "Сколько зараженных на данный момент":
        await bot.send_message(message.from_user.id, f'Заражено на данный момент {ps.parser()}')
    elif message.text == "Узнать прогноз":
        await bot.send_message(message.from_user.id, "Введите название города ")
    elif message.text == "Интересное о COVID-19":
        await bot.send_message(message.from_user.id, "Интересное о COVID-19", reply_markup=nav.otherMenu)
    elif message.text == "Факты о COVID-19":
        await bot.send_message(message.from_user.id, rt.arbitrary())
    elif message.text == "Назад":
        await bot.send_message(message.from_user.id, "Интересное о COVID-19", reply_markup=nav.mainMenu)
    elif message.text == "Профилактика COVID-19":
        await bot.send_message(message.from_user.id, "Профилактика COVID-19", reply_markup=nav.preventionMenu)
    elif message.text == "Симптомы":
        await asyncio.sleep(1.0)
        await message.reply("1.Высокая температура.")
        await asyncio.sleep(1.0)
        await message.reply("2.Затрудненное дыхание.")
        await asyncio.sleep(1.0)
        await message.reply("3.Чихание, кашель и заложенность носа.")
        await asyncio.sleep(1.0)
        await message.reply("4.Боли в мышцах и в груди.")
        await asyncio.sleep(1.0)
        await message.reply("5.Головная боль и слабость.")
        await asyncio.sleep(1.0)
        await message.reply("6.Возможна тошнота, рвота и диарея.")
        await asyncio.sleep(1.0)
    elif message.text == "Профилактика":
        await asyncio.sleep(0.5)
        await message.reply("Мойте руки")
        await asyncio.sleep(3.0)
        await message.reply("Всегда мойте руки: когда приходите на работу или возвращаетесь домой. "
                            "Для профилактики также подойдут влажные салфетки или дезинфицирующие растворы.")
        await asyncio.sleep(0.5)
        await message.reply("Помните о необходимости соблюдать меры профилактики, как только вышли из дома")
        await asyncio.sleep(3.0)
        await message.reply("Избегайте ненужных поездок и не ходите в места массового скопления людей.")
        await asyncio.sleep(0.5)
        await message.reply("Не трогайте лицо руками")
        await asyncio.sleep(3.0)
        await message.reply("Не подносите руки к носу и глазам. Быстрее всего вирус попадает "
                            "в организм через слизистую оболочку. Когда чихаете всегда прикрывайтесь платком.")
        await asyncio.sleep(0.5)
        await message.reply("Отмените путешествия")
        await asyncio.sleep(3.0)
        await message.reply("На время, пока разные страны мира борются с корона вирусом, не следует путешествовать "
                            "заграницу. В особенности туда, где ситуация с коронавирусом крайне тяжелая.")
        await asyncio.sleep(0.5)
        await message.reply("Вакцинируйтесь")
        await asyncio.sleep(3.0)
        await message.reply("Вакцина – единственное надежное средство профилактики вируса. Только пройдя вакцинацию "
                            "мы сможем остановить передачу вируса и защитить себя от его тяжелых последствий.")
    else:
        try:
            prediction, real, miss = get_city_prediction(message.text)
            await message.answer(f"{prediction} - предсказание нашей модели машинного обучения. \n"
                                 f"{real} - показатель из размеченных профессионалами данных. \n"
                                 f"Погрешность составила {miss}.")
        except:
            await message.reply("Такого города нет в нашей базе.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
