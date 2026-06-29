import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# التوكن الخاص بك
TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

# إنشاء مجلد لتخزين البوتات إذا لم يكن موجوداً
if not os.path.exists("my_bots"):
    os.makedirs("my_bots")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # التأكد أن الملف هو ملف بايثون
    if not update.message.document.file_name.endswith('.py'):
        await update.message.reply_text("يرجى إرسال ملف بصيغة .py فقط")
        return

    # تحميل الملف
    file = await update.message.document.get_file()
    file_path = os.path.join("my_bots", update.message.document.file_name)
    await file.download_to_drive(file_path)
    
    await update.message.reply_text(f"تم حفظ الملف: {update.message.document.file_name}\nجاري التشغيل...")

    try:
        # تشغيل الملف في الخلفية
        process = subprocess.Popen(["python3", file_path])
        await update.message.reply_text(f"✅ تم تشغيل البوت بنجاح! \nمعرف العملية (PID): {process.pid}")
    except Exception as e:
        await update.message.reply_text(f"❌ حدث خطأ أثناء التشغيل: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # استقبال الملفات
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    print("البوت يعمل الآن...")
    app.run_polling()
