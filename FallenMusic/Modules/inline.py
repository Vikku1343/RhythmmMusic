# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from FallenMusic import BOT_NAME, app


@app.on_inline_query()
async def inline_query_handler(_, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await app.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="𝕥𝕪𝕡𝕖 𝕤𝕠𝕞𝕖𝕥𝕚𝕙𝕚𝕟𝕘 𝕥𝕠 𝕤𝕖𝕒𝕣𝕔𝕙 𝕠𝕟 𝕪𝕠𝕦𝕥𝕦𝕓𝕖...",
                cache_time=1
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• 𝕪𝕠𝕦𝕥𝕦𝕓𝕖 •",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
✨ **𝕥𝕚𝕥𝕝𝕖:** [{title}]({link})

⏳ **𝕕𝕦𝕣𝕒𝕒𝕥𝕚𝕠𝕟 :** `{duration}`ᴍɪɴᴜᴛᴇs
👀 **𝕧𝕚𝕖𝕨𝕤 :** `{views}`
⏰ **𝕡𝕦𝕓𝕝𝕚𝕤𝕙𝕖𝕕 𝕠𝕟 :** {published}
🎥 **𝕔𝕙𝕒𝕟𝕟𝕖𝕝 :** [{channel}]({channellink})

<u>💖 **𝕤𝕖𝕒𝕣𝕔𝕙 𝕡𝕠𝕨𝕖𝕣𝕖𝕕 𝕓𝕪 {BOT_NAME}**</u>"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await app.answer_inline_query(query.id, results=answers)
        except:
            return
