from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from BWFMUSIC import app
from BWFMUSIC.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭"
        logger_text = f""" 💌➖➖➖➖➖➖➖➖➖🍒     
**{MUSIC_BOT_NAME} 𓆩〭⃛〬🤍𝐏𝐥𝐚𝐲♕︎𝐋𝐨𝐠𝐠𝐞𝐫🥀⍣⃪͜𓆪**
┏━━━━━━━━━━━━━━━━━┓
   🎀『𝐂𝐡𝐚𝐭』🦋𝐈𝐧𝐟𝐨🙈
┗━━━━━━━━━━━━━━━━━┛   
➖➖➖➖➖➖➖➖➖➖➖
┣**❣️𝐂𝐡𝐚𝐭💨** {message.chat.title} [`{message.chat.id}`]
➖➖➖➖➖➖➖➖➖➖➖
┣**♦️𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤♦** {chatusername}
➖➖➖➖➖➖➖➖➖➖➖
┣**🍷 𝐔ʀ 𝐈d 💖** {message.from_user.mention}
➖➖➖➖➖➖➖➖➖➖➖
┣**🥀✰𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ♦️ꭙ:** @{message.from_user.username}
➖➖➖➖➖➖➖➖➖➖➖
┣**🌷𝐈⚚‎𝐝🔥** `{message.from_user.id}`
➖➖➖➖➖➖➖➖➖➖➖
┣**🕊⃟♥️𝐒𝐞𝐚𝐫𝐜𝐡 𝐒𝐨𝐧𝐠⚚‎•👁** {message.text}
➖➖➖➖➖➖➖➖➖➖➖

┣**👻𝐒𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞✨🍃** {streamtype}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
