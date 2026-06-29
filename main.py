from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

# قاموس يحتوي على 30 أداة
CODES = {
    "down_yt": {"text": "تحميل يوتيوب", "lib": "pip install yt-dlp", "code": "import yt_dlp\n# كود التحميل..."},
    "cyber_nmap": {"text": "فحص Nmap", "lib": "pip install python-nmap", "code": "import nmap\n# فحص الثغرات..."},
    "ai_img": {"text": "توليد صور", "lib": "pip install openai", "code": "from openai import OpenAI..."},
    "web_scrape": {"text": "سحب بيانات", "lib": "pip install bs4", "code": "from bs4 import BeautifulSoup..."},
    "bot_crypto": {"text": "بوت تداول", "lib": "pip install ccxt", "code": "import ccxt..."},
    "email_sender": {"text": "إرسال إيميلات", "lib": "pip install secure-smtplib", "code": "import smtplib..."},
    "db_sqlite": {"text": "قاعدة بيانات", "lib": "مدمجة", "code": "import sqlite3..."},
    "qr_gen": {"text": "صانع QR", "lib": "pip install qrcode", "code": "import qrcode..."},
    "pdf_tool": {"text": "تعديل PDF", "lib": "pip install PyPDF2", "code": "import PyPDF2..."},
    "weather_bot": {"text": "بوت طقس", "lib": "pip install requests", "code": "import requests..."},
    "trans_bot": {"text": "ترجمة نصوص", "lib": "pip install googletrans", "code": "from googletrans import Translator..."},
    "game_bot": {"text": "بوت ألعاب", "lib": "pip install telegram", "code": "# منطق اللعبة..."},
    "music_dl": {"text": "تحميل موسيقى", "lib": "pip install spotdl", "code": "from spotdl import Spotdl..."},
    "file_conv": {"text": "تحويل صيغ", "lib": "pip install moviepy", "code": "from moviepy.editor import *..."},
    "proxy_bot": {"text": "فحص بروكسي", "lib": "pip install requests", "code": "import requests..."},
    "auto_msg": {"text": "رسائل تلقائية", "lib": "pip install pyautogui", "code": "import pyautogui..."},
    "insta_dl": {"text": "تحميل انستجرام", "lib": "pip install instaloader", "code": "import instaloader..."},
    "sys_info": {"text": "مراقب سيرفر", "lib": "pip install psutil", "code": "import psutil..."},
    "pass_gen": {"text": "مولد كلمات سر", "lib": "مدمجة", "code": "import secrets..."},
    "calc_bot": {"text": "حاسبة علمية", "lib": "لا تحتاج", "code": "import math..."},
    "short_url": {"text": "تقصير روابط", "lib": "pip install pyshorteners", "code": "import pyshorteners..."},
    "ping_test": {"text": "فحص Ping", "lib": "pip install ping3", "code": "import ping3..."},
    "crypto_hash": {"text": "تشفير نصوص", "lib": "pip install hashlib", "code": "import hashlib..."},
    "clock_bot": {"text": "تنبيهات ومؤقت", "lib": "pip install schedule", "code": "import schedule..."},
    "stock_bot": {"text": "أسعار الأسهم", "lib": "pip install yfinance", "code": "import yfinance..."},
    "joke_bot": {"text": "بوت نكت", "lib": "pip install pyjokes", "code": "import pyjokes..."},
    "wiki_bot": {"text": "بحث ويكيبيديا", "lib": "pip install wikipedia", "code": "import wikipedia..."},
    "code_run": {"text": "مشغل بايثون", "lib": "لا تحتاج", "code": "exec(code_str)..."},
    "backup_bot": {"text": "نسخ احتياطي", "lib": "pip install shutil", "code": "import shutil..."},
    "ping_server": {"text": "فحص اتصال", "lib": "pip install requests", "code": "import requests..."}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = list(CODES.keys())
    keyboard = []
    # توزيع الـ 30 زر في 15 صفاً
    for i in range(0, 30, 2):
        keyboard.append([
            InlineKeyboardButton(CODES[keys[i]]['text'], callback_data=keys[i]),
            InlineKeyboardButton(CODES[keys[i+1]]['text'], callback_data=keys[i+1])
        ])
    
    await update.message.reply_text("📚 **مكتبة البوتات الاحترافية (30 أداة)**\nاختر الأداة المطلوبة:", 
                                   reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

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
    print("البوت يعمل...")
    app.run_polling()
