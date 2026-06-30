import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# التوكن الخاص بك
API_TOKEN = '8759630215:AAHgnCzJX-JPwgUqTwZtWdXXVUWR4D-la30'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أرسل رابط تيك توك وسأحاول معالجته.")

@dp.message()
async def process_link(message: types.Message):
    url = message.text
    if "tiktok.com" in url:
        await message.answer("جاري الاتصال بالسيرفر، يرجى الانتظار...")
        
        # قالب لطلب HTTP
        try:
            # هنا ستضع رابط الـ API الذي ستجده لاحقاً
            # response = requests.post("URL_HERE", data={"url": url})
            
            # محاكاة لنجاح العملية
            await message.answer("تم إرسال الطلب بنجاح إلى النظام!")
        except Exception as e:
            await message.answer(f"حدث خطأ أثناء الاتصال: {str(e)}")
    else:
        await message.answer("رابط غير صالح.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
