import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! أرسل لي يوزر التيك توك (بدون @).")

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "").strip()
    await update.message.reply_text("جاري استخراج البيانات...")
    
    # استخدام رابط API بديل يعطي بيانات أكثر دقة
    url = f"https://tik.fail/api/user?unique_id={username}"
    
    try:
        response = requests.get(url, timeout=15).json()
        
        # التأكد من نجاح العملية (تختلف رموز النجاح حسب الـ API)
        if response and "user" in response:
            user = response["user"]
            stats = response.get("stats", {})
            
            # محاولة الحصول على الدولة بأكثر من طريقة
            region = user.get("region") or user.get("location") or "غير معروف"
            avatar_url = user.get("avatar_large") or user.get("avatar")
            
            caption = (
                f"👤 الاسم: {user.get('nickname')}\n"
                f"🆔 اليوزر: @{user.get('unique_id')}\n"
                f"🌍 الدولة: {region}\n"
                f"👥 المتابعون: {stats.get('followerCount')}\n"
                f"❤️ الإعجابات: {stats.get('heartCount')}\n"
                f"📝 البايو: {user.get('signature')}"
            )
            
            if avatar_url:
                await update.message.reply_photo(photo=avatar_url, caption=caption)
            else:
                await update.message.reply_text(caption)
        else:
            await update.message.reply_text("لم يتم العثور على معلومات للحساب، تأكد من اليوزر.")
            
    except Exception as e:
        await update.message.reply_text(f"خطأ في الاتصال: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), get_tiktok_user))
    app.run_polling()
