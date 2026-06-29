import os
import subprocess
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# إعداد السجلات لمراقبة أخطاء البوت في Railway
logging.basicConfig(level=logging.INFO)

# التوكن الخاص بك
TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

# إنشاء مجلد لتخزين البوتات إذا لم يكن موجوداً
if not os.path.exists("my_bots"):
    os.makedirs("my_bots")

# دالة الاستجابة للأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("تم استلام أمر /start")
    await update.message.reply_text("أهلاً بك! أنا جاهز لاستقبال ملفات البوت. أرسل لي أي ملف .py وسأقوم بتشغيله.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"جاري معالجة ملف: {update.message.document.file_name}")
    
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
        print(f"تم تشغيل {update.message.document.file_name} بمعرف عملية: {process.pid}")
        await update.message.reply_text(f"✅ تم تشغيل البوت بنجاح! \nمعرف العملية (PID): {process.pid}")
    except Exception as e:
        print(f"خطأ: {e}")
        await update.message.reply_text(f"❌ حدث خطأ أثناء التشغيل: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    # استقبال الملفات
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    print("البوت يعمل الآن وينتظر الأوامر...")
    app.run_polling()
