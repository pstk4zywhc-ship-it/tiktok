import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = "8558689070:AAEghtAedZya9RZ1S22sS0x8HPTLwQyq_oA"

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "").strip()
    await update.message.reply_text("جاري الفحص...")
    
    url = f"https://www.tikwm.com/api/user/info?unique_id={username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        # طباعة الرد الخام لمعرفة سبب المشكلة
        print(f"Raw Response: {response.text}")
        
        data = response.json()
        
        if data.get("code") == 0:
            user = data["data"]["user"]
            stats = data["data"]["stats"]
            caption = f"👤 الاسم: {user.get('nickname')}\n🌍 الدولة: {user.get('region', 'غير معروف')}"
            await update.message.reply_photo(photo=user.get('avatar'), caption=caption)
        else:
            await update.message.reply_text(f"خطأ من الموقع: {data.get('msg')}")
            
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ تقني: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), get_tiktok_user))
    app.run_polling()
