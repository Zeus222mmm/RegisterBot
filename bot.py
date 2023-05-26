import logging 

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from btn import *


BOT_TOKEN = "6016968662:AAFiSwA24j9uBOy01lGJWppy9rTV8lkHK8M"


logging.basicConfig(level=logging.INFO)

# bot = Bot(token=BOT_TOKEN, parse_mode='html')
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

info = {
    "name" : "",
    "age" : 0, 
    "address" : "",
}

class Meningstatelarim(StatesGroup):
    ism = State()
    yosh = State()
    ad = State()

@dp.message_handler(commands=['start'])
async def send_well(message: types.Message):
    btn = await start_menu_btn()
    await message.answer(f"<b>Hi!</b>, bu sizning firstnameningiz:  <span class= 'tg-spoiler'>{message.from_user.first_name}</span>, bu sizning nicknameningiz: <span class= 'tg-spoiler'>{message.from_user.last_name}</span>,", reply_markup=btn)
    # await message.answer("<strong>Hi!</strong>")
    # await message.answer("<i>Hi!</i>")
    # await message.answer("<em>Hi!</em>")
    # await message.answer("<a href='t.me/POSSIBLE'>Hello</a>", disable_web_page_preview= True)
    # await message.answer("<u>Hi!</u>")
    # await message.answer("<ins>Hi!</ins>")
    # await message.answer("<s>Hi!</s>")
    # await message.answer("<strike>Hi!</strike>")
    # await message.answer("<del>Hi!</del>")
    # await message.answer("<span class='tg-spoiler'>Hi!</span>")
    # await message.answer("<b>bold <i>italic bold <s>italic bold strikethrough <span class='tg-spoiler'>italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>")
    # await message.answer("<a href='tg://user?id=123456789'>inline mention of a user</a>")
    # await message.answer("<tg-emoji emoji-id='5368324170671202286'>👍</tg-emoji>")
    # await message.answer("<pre>pre-formatted fixed-width code block</pre>")
    # await message.answer("<pre><code class='language-python'>pre-formatted fixed-width code block written in the Python programming language</code></pre>")




@dp.message_handler(text="👤 Admin bilan aloqa")
async def support_handler2(message: types.Message):
    await message.answer("Bot admini: @winchestor_dev")


@dp.message_handler(text="🖇 Ro'yxatdan o'tish")
async def register_handler(message: types.Message):
    await message.answer("Ismingizni kirirting: ")

    await Meningstatelarim.ism.set()

@dp.message_handler(state=Meningstatelarim.ism)
async def ism_date(message: types.Message):

    print(message.text)
    info["name"]=message.text
    await message.answer("Yoshingizni kirirting: ")
    await Meningstatelarim.yosh.set()

@dp.message_handler(state=Meningstatelarim.yosh)
async def ism_date(message: types.Message):
    print(message.text)
    info["age"]=message.text
    await message.answer("Addresingizni kirirting: ")
    await Meningstatelarim.ad.set()

@dp.message_handler(state=Meningstatelarim.ad)
async def ism_date(message: types.Message, state: FSMContext):
    print(message.text)
    info["address"]=message.text
    btn = await info_yes_or_no_btn()
    await message.answer(f"Ism: {info['name']}\n Yosh:{info['age']}\n Manzil: {info['address']}" , reply_markup=btn)


@dp.callback_query_handler(text="yes")
async def answer_yes_callback(call: types.CallbackQuery):
    # await call.answer("Siz rozi bo'ldingiz!",  show_alert=True)
    btn =  await start_menu_btn()
    await call.message.answer("Siz ro'yhatan o'tingiz!", reply_markup=btn)
     

@dp.callback_query_handler(text="no")
async def answer_no_callback(call: types.CallbackQuery):
    # await call.answer("siz rozi masmisiz", show_alert=True) 
    btn =  await start_menu_btn()
    await call.message.answer("siz ro'yhatan o'tmadingiz", reply_markup=btn)

if __name__ =="__main__":
    executor.start_polling(dp)