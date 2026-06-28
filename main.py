from TikTokApi import TikTokApi
import asyncio

# ... (باقي الكود كما هو)

async def get_tiktok_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.replace("@", "").strip()
    await update.message.reply_text("جاري جلب البيانات...")

    try:
        async with TikTokApi() as api:
            # هنا التعديل: سنحاول الاتصال بدون توكن
            await api.create_sessions(num_sessions=1, sleep_after=3)
            user = api.user(username=username)
            user_data = await user.info()
            
            # ... (باقي الكود لإرسال المعلومات)
