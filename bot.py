import logging

from aiogram import Bot, Dispatcher,executor,types
import qrcode
import os


logging.basicConfig(level=logging.INFO)




BOT_TOKEN = "6016968662:AAFiSwA24j9uBOy01lGJWppy9rTV8lkHK8M"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['start'])
async def start_bot_handler(message: types.Message):
    await message.answer("Assalomu aleykum.\n\nBu bot orqali siz QR kod yasay olasiz!")


@dp.message_handler(content_types=['text'])
async def generate_qrcode_handler(message: types.Message):
    img = qrcode.make(message.text)
    filename = "qr_result.png"
    img.save(filename)
    await message.answer_photo(types.InputFile(filename), caption="✅ Tayyor, https://pypi.org/project/qrcode/")
    os.unlink(filename)

if __name__ == '__main__':
    executor.start_polling(dp)