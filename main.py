try:
    response = requests.get(url, timeout=10).json()
    if response.get("code") == 0:
        # (الكود القديم الخاص بك هنا...)
    else:
        await update.message.reply_text(f"خطأ من الموقع: {response.get('msg', 'غير معروف')}")
except Exception as e:
    # هنا سنعرف سبب الخطأ الحقيقي
    print(f"Error details: {e}") 
    await update.message.reply_text(f"حدث خطأ: {str(e)}")
