import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ضع التوكن الخاص بك هنا
API_TOKEN = 'import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ضع التوكن الخاص بك هنا
API_TOKEN = 'YOUR_TOKEN_HERE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("البوت يعمل الآن! أرسل رابط الفيديو للبدء.")

@dp.message()
async def echo(message: types.Message):
    # هذا المكان الذي ستضيف فيه منطق البرمجة الخاص بك
    await message.answer(f"لقد استلمت الرابط: {message.text}")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("البوت يعمل الآن! أرسل رابط الفيديو للبدء.")

@dp.message()
async def echo(message: types.Message):
    # هذا المكان الذي ستضيف فيه منطق البرمجة الخاص بك
    await message.answer(f"لقد استلمت الرابط: {message.text}")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
