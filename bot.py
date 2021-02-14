import config
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import API_TOKEN
from voice import text_to_speech

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Echo bot
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

# Спикалка
@dp.message_handler()
async def reply(message: types.Message):
    voice_file = text_to_speech(message.text)
    vf = open(voice_file, "rb")
    await message.reply_voice(voice=vf)


""" @dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
 """

# run pooling
if __name__ == '__main__':
    executor.start_polling(dp)
