import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد السجلات (Log) لمعرفة حالة البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# جلب التوكن من إعدادات الاستضافة (Environment Variables)
TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! أنا بوت المباريات جاهز للعمل.")

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هنا ستظهر روابط البث المباشر قريباً.")

if __name__ == '__main__':
    if not TOKEN:
        print("خطأ: لم يتم العثور على التوكن! تأكد من إضافته في إعدادات البيئة.")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("live", live))
        
        print("البوت يعمل الآن...")
        app.run_polling()
