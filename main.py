        if response.get("code") == 0:
            user = response["data"]["user"]
            stats = response["data"]["stats"]
            avatar_url = user.get('avatar')
            
            caption = (
                f"👤 الاسم: {user.get('nickname')}\n"
                f"👥 المتابعون: {stats.get('followerCount')}\n"
                f"❤️ الإعجابات: {stats.get('heartCount')}"
            )
            
            # إرسال الصورة إذا وجد رابط، وإلا إرسال النص فقط
            if avatar_url:
                await update.message.reply_photo(photo=avatar_url, caption=caption)
            else:
                await update.message.reply_text(caption)
        else:
            await update.message.reply_text("لم أجد هذا المستخدم، تأكد من اليوزر.")
