from telegraph import upload_file
from pyrogram import filters
from BWFMUSIC import app


@app.on_message(filters.command('tgm','link'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("🔥ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...ʙʏ •ʙω͠ғ• ᴍᴜsɪᴄ🦋💔")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'🇾ᴏᴜʀ🇹ᴇʟᴇɢʀᴀᴘʜ 💫 {url}')
