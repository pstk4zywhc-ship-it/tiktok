import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from TikTokApi import TikTokApi
import asyncio

# إعداد السجل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# التوكن مدمج
TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! أرسل لي اسم المستخدم (Username) لأي حساب تيك توك وسأعطيك معلوماته.")

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "").strip()
    await update.message.reply_text("جاري جلب البيانات، يرجى الانتظار...")

    try:
        async with TikTokApi() as api:
            # ملاحظة: ضع الـ ms_token الخاص بك هنا لضمان عمل الاستعلام
            await api.create_sessions(ms_tokens=["YOUR_MS_TOKEN_HERE"], num_sessions=1, sleep_after=3)
            user = api.user(username=username)
            user_data = await user.info()
            
            info = user_data.get('user', {})
            stats = user_data.get('stats', {})
            
            caption = (
                f"👤 **الاسم:** {info.get('nickname', 'غير متوفر')}\n"
                f"🌍 **الدولة:** {info.get('region', 'غير متوفر')}\n"
                f"👥 **المتابعون:** {stats.get('followerCount', 0)}\n"
                f"❤️ **الإعجابات:** {stats.get('heartCount', 0)}\n"
                f"📝 **البايو:** {info.get('signature', 'لا يوجد')}"
            )
            
            await update.message.reply_photo(photo=info.get('avatarLarger'), caption=caption)
            
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: تأكد من اسم المستخدم أو حاول لاحقاً.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), get_tiktok_user))
    print("البوت يعمل الآن...")
    app.run_polling()
