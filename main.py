from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

# بيانات الأكواد
CODES = {
    "downloader": {
        "text": "بوت تحميل فيديوهات (yt-dlp)",
        "lib": "المكتبة: pip install yt-dlp",
        "code": "```python\nimport yt_dlp\n# كود التحميل هنا...\n```"
    },
    "cyber": {
        "text": "بوت أمن سيبراني (أدوات)",
        "lib": "المكتبة: pip install requests",
        "code": "```python\n# كود أدوات الأمن هنا...\n```"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("بوت تحميل", callback_data='downloader')],
        [InlineKeyboardButton("بوت أمن سيبراني", callback_data='cyber')]
    ]
    await update.message.reply_text("اختر البوت الذي تريد كوده:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = CODES.get(query.data)
    
    response = f"**{data['text']}**\n\n{data['lib']}\n\n{data['code']}"
    await query.message.reply_text(response, parse_mode='Markdown')
    await query.answer()

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.run_polling()
