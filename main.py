from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

# قاموس يحتوي على 20 بوت مع مكتباتهم وأكوادهم
CODES = {
    "down_yt": {"text": "تحميل يوتيوب", "lib": "pip install yt-dlp", "code": "import yt_dlp..."},
    "cyber_nmap": {"text": "فحص Nmap", "lib": "pip install python-nmap", "code": "import nmap..."},
    "ai_img": {"text": "توليد صور", "lib": "pip install openai", "code": "from openai import OpenAI..."},
    "web_scrape": {"text": "سحب بيانات", "lib": "pip install beautifulsoup4", "code": "from bs4 import BeautifulSoup..."},
    "bot_crypto": {"text": "بوت تداول", "lib": "pip install ccxt", "code": "import ccxt..."},
    "email_sender": {"text": "إرسال إيميلات", "lib": "pip install secure-smtplib", "code": "import smtplib..."},
    "db_sqlite": {"text": "قاعدة بيانات", "lib": "لا تحتاج (مدمجة)", "code": "import sqlite3..."},
    "qr_gen": {"text": "صانع QR", "lib": "pip install qrcode", "code": "import qrcode..."},
    "pdf_tool": {"text": "تعديل PDF", "lib": "pip install PyPDF2", "code": "import PyPDF2..."},
    "weather_bot": {"text": "بوت طقس", "lib": "pip install requests", "code": "import requests..."},
    "trans_bot": {"text": "بوت ترجمة", "lib": "pip install googletrans==4.0.0-rc1", "code": "from googletrans import Translator..."},
    "game_bot": {"text": "بوت ألعاب", "lib": "pip install python-telegram-bot", "code": "# logic here..."},
    "music_dl": {"text": "تحميل موسيقى", "lib": "pip install spotdl", "code": "from spotdl import Spotdl..."},
    "file_conv": {"text": "تحويل ملفات", "lib": "pip install moviepy", "code": "from moviepy.editor import *..."},
    "proxy_bot": {"text": "فحص بروكسي", "lib": "pip install requests", "code": "import requests..."},
    "auto_msg": {"text": "رسائل تلقائية", "lib": "pip install pyautogui", "code": "import pyautogui..."},
    "insta_dl": {"text": "تحميل انستجرام", "lib": "pip install instaloader", "code": "import instaloader..."},
    "sys_info": {"text": "مراقب سيرفر", "lib": "pip install psutil", "code": "import psutil..."},
    "pass_gen": {"text": "صانع باسورد", "lib": "لا تحتاج", "code": "import secrets..."},
    "calc_bot": {"text": "بوت حاسبة", "lib": "لا تحتاج", "code": "def calculate():..."}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إنشاء قائمة أزرار 20 (كل سطر زرين)
    keys = list(CODES.keys())
    keyboard = []
    for i in range(0, 20, 2):
        keyboard.append([
            InlineKeyboardButton(CODES[keys[i]]['text'], callback_data=keys[i]),
            InlineKeyboardButton(CODES[keys[i+1]]['text'], callback_data=keys[i+1])
        ])
    
    await update.message.reply_text("اختر الأداة التي تريد كودها:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = CODES.get(query.data)
    
    response = f"📌 **{data['text']}**\n\n🔹 {data['lib']}\n\n```python\n{data['code']}\n```"
    await query.message.reply_text(response, parse_mode='Markdown')
    await query.answer()

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.run_polling()
