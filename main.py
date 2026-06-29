import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

# إعداد السجلات
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إنشاء قائمة من 20+ زر (مقسمة لصفوف)
    keyboard = [
        [InlineKeyboardButton("فحص المواقع (Nmap)", callback_data='nmap'), InlineKeyboardButton("تحليل الشبكات", callback_data='net')],
        [InlineKeyboardButton("اختبار ثغرات (SQLi)", callback_data='sqli'), InlineKeyboardButton("فحص XSS", callback_data='xss')],
        [InlineKeyboardButton("تشفير (Hash)", callback_data='hash'), InlineKeyboardButton("فك تشفير", callback_data='unhash')],
        [InlineKeyboardButton("معلومات IP", callback_data='ip'), InlineKeyboardButton("البحث عن ثغرات", callback_data='cve')],
        [InlineKeyboardButton("أدوات Wifi", callback_data='wifi'), InlineKeyboardButton("هجمات DOS", callback_data='dos')],
        [InlineKeyboardButton("فحص SSL", callback_data='ssl'), InlineKeyboardButton("أدوات استطلاع", callback_data='recon')],
        [InlineKeyboardButton("تخطي حماية", callback_data='bypass'), InlineKeyboardButton("أدوات OSINT", callback_data='osint')],
        [InlineKeyboardButton("مكتبة الثغرات", callback_data='exploit'), InlineKeyboardButton("فحص الملفات", callback_data='malware')],
        [InlineKeyboardButton("أوامر Linux", callback_data='linux'), InlineKeyboardButton("أدوات التشفير", callback_data='crypto')],
        [InlineKeyboardButton("تحديث الأدوات", callback_data='update'), InlineKeyboardButton("الدعم الفني", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحباً بك في بوت الأمن السيبراني. اختر الأداة المطلوبة:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"جاري تشغيل الأداة: {query.data} ...")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("البوت يعمل الآن...")
    app.run_polling()
