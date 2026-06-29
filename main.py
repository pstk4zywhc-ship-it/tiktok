import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # تحميل الملف المرسل
    file = await update.message.document.get_file()
    file_path = f"./bots/{update.message.document.file_name}"
    
    # حفظ الملف في مجلد 'bots'
    await file.download_to_drive(file_path)
    
    await update.message.reply_text(f"تم استلام الملف {update.message.document.file_name}. جاري التشغيل...")
    
    # تشغيل الملف كعملية منفصلة
    try:
        subprocess.Popen(["python3", file_path])
        await update.message.reply_text("✅ تم تشغيل البوت بنجاح!")
    except Exception as e:
        await update.message.reply_text(f"❌ حدث خطأ أثناء التشغيل: {e}")

# (يجب إضافة Handler لفلتر الملفات .py)
