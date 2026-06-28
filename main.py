import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from TikTokApi import TikTokApi
import asyncio

# إعداد السجل لمتابعة الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# مفتاح البوت (يفضل استخدام متغيرات البيئة Environment Variables لاحقاً)
TOKEN = "ضع_توكن_البوت_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! أرسل لي اسم المستخدم (Username) لأي حساب تيك توك وسأعطيك معلوماته.")

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "") # تنظيف اليوزر
    await update.message.reply_text("جاري جلب البيانات، يرجى الانتظار...")

    try:
        async with TikTokApi() as api:
            # ملاحظة: يجب وضع ms_token في بيئة الاستضافة
            await api.create_sessions(ms_tokens=["ضع_الـ_ms_token_هنا"], num_sessions=1, sleep_after=3)
            user = api.user(username=username)
            user_data = await user.info()
            
            info = user_data['user']
            stats = user_data['stats']
            
            caption = (
                f"👤 **الاسم:** {info.get('nickname')}\n"
                f"🌍 **الدولة:** {info.get('region')}\n"
                f"👥 **المتابعون:** {stats.get('followerCount')}\n"
                f"❤️ **الإعجابات:** {stats.get('heartCount')}\n"
                f"📝 **البايو:** {info.get('signature')}"
            )
            
            # إرسال الصورة والمعلومات
            await update.message.reply_photo(photo=info.get('avatarLarger'), caption=caption)
            
    except Exception as e:
        await update.message.reply_text(f"عذراً، حدث خطأ أثناء جلب البيانات: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), get_tiktok_user))
    
    print("البوت يعمل الآن...")
    app.run_polling()
