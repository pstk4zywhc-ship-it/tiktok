import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل لي اسم المستخدم (Username) وسأجلب لك معلوماته.")

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "").strip()
    await update.message.reply_text("جاري جلب البيانات...")

    # نستخدم API خارجي بسيط وسريع
    url = f"https://www.tikwm.com/api/user/info?unique_id={username}"
    
    try:
        response = requests.get(url).json()
        if response.get("code") == 0:
            user = response["data"]["user"]
            stats = response["data"]["stats"]
            
            caption = (
                f"👤 الاسم: {user.get('nickname')}\n"
                f"🆔 اليوزر: @{user.get('unique_id')}\n"
                f"👥 المتابعون: {stats.get('followerCount')}\n"
                f"❤️ الإعجابات: {stats.get('heartCount')}\n"
                f"📝 البايو: {user.get('signature')}"
            )
            await update.message.reply_photo(photo=user.get('avatar'), caption=caption)
        else:
            await update.message.reply_text("لم أجد هذا المستخدم، تأكد من الاسم.")
    except Exception as e:
        await update.message.reply_text("حدث خطأ في الاتصال، حاول لاحقاً.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), get_tiktok_user))
    app.run_polling()
