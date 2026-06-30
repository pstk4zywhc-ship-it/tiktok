import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import yt_dlp

API_TOKEN = '8759630215:AAHgnCzJX-JPwgUqTwZtWdXXVUWR4D-la30'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أهلاً بك! أرسل رابط تيك توك لأجلب لك بيانات الفيديو.")

@dp.message()
async def process_link(message: types.Message):
    url = message.text
    if "tiktok.com" in url:
        await message.answer("جاري جلب بيانات الفيديو من تيك توك...")
        
        try:
            # استخدام yt_dlp لجلب البيانات
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'غير معروف')
                views = info.get('view_count', 'غير متاح')
                
                await message.answer(f"✅ تم العثور على الفيديو!\n\n📝 العنوان: {title}\n👁 المشاهدات: {views}")
        except Exception as e:
            await message.answer(f"عذراً، لم أتمكن من جلب البيانات. (الرابط قد يكون خاصاً).")
    else:
        await message.answer("الرجاء إرسال رابط تيك توك صالح.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

