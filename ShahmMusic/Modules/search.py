
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from ShahmMusic import app


@app.on_message(filters.command(["search"]) | filters.command(["بحث","يوت"],prefixes= ["/", "!","","#"]))
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("⌔︙ اكتب شي تريد تبحث علي")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("جاري البحث ..🚦")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"⌔︙ العـنوان : {results[i]['title']}\n"
            text += f"⌔︙ المـدة : `{results[i]['duration']}`\n"
            text += f"⌔︙ المـشاهدات : `{results[i]['views']}`\n"
            text += f"⌔︙ القـناه : {results[i]['channel']}\n"
            text += f"⌔︙ الـرابط : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="اقفل",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
