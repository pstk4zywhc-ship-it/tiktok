import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! أرسل لي يوزر التيك توك وسأجلب لك معلوماته.")

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "").strip()
    await update.message.reply_text("جاري جلب البيانات من السيرفر...")
    
    # استخدام رابط API بديل قد يوفر بيانات أكثر دقة
    url = f"https://api.tikwm.com/api/user/info?unique_id={username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20).json()
        
        if response.get("code") == 0:
            user = response["data"]["user"]
            stats = response["data"]["stats"]
            avatar_url = user.get('avatar_larger') or user.get('avatar')
            
            # محاولة قراءة الدولة من إعدادات الحساب أو إحداثيات الموقع
            region = user.get('region') or "غير متاح حالياً"
            
            caption = (
                f"👤 الاسم: {user.get('nickname')}\n"
                f"🆔 اليوزر: @{user.get('unique_id')}\n"
                f"🌍 الدولة/المنطقة: {region}\n"
                f"👥 المتابعون: {stats.get('followerCount')}\n"
                f"❤️ الإعجابات: {stats.get('heartCount')}\n"
                f"📝 البايو: {user.get('signature')}"
            )
            
            # إرسال الصورة دائماً
            if avatar_url:
                await update.message.reply_photo(photo=avatar_url, caption=caption)
            else:
                await update.message.reply_text(caption)
        else:
            await update.message.reply_text("عذراً، لم أجد هذا المستخدم، تأكد من صحة اليوزر.")
            
    except Exception as e:
        await update.message.reply_text(f"خطأ في الاتصال: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), get_tiktok_user))
    app.run_polling()
