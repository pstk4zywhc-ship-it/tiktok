import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# التوكن المدمج
API_TOKEN = '8759630215:AAHgnCzJX-JPwgUqTwZtWdXXVUWR4D-la30'

# إعدادات البوت
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# رسالة البدء
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("أهلاً بك! البوت جاهز الآن. أرسل لي رابط تيك توك.")

# استقبال الروابط
@dp.message()
async def echo_handler(message: types.Message):
    if "tiktok.com" in message.text:
        await message.answer("جاري معالجة الرابط، يرجى الانتظار...")
        # هنا سيتم لاحقاً ربط دوال الـ Request
    else:
        await message.answer("الرجاء إرسال رابط صحيح من تيك توك.")

# تشغيل البوت
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
