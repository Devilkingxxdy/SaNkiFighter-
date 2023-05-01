from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "𝐒𝐚𝐍𝐤𝐢𝐅𝐢𝐠𝐇𝐭𝐞𝐫"
pic = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/5f88061d369958ee0fedd.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐒𝐚𝐍𝐤𝐢𝐅𝐢𝐠𝐇𝐭𝐞𝐫 - 𝙱𝚢 𝙳𝚎𝚟𝚒𝚕𝚔𝚒ñ𝚐"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **𝙼à𝚜𝚝𝚎𝚛:** {owner_mention}
➠ **𝙿𝚢𝚝𝙷𝚘𝚗 𝚅𝚎𝚛𝚂𝚘𝚒𝚗:** `{platform.python_version()}`
➠ **𝚂𝚊𝙽𝚔𝚒𝙵𝚒𝚐𝙷𝚝𝚎𝚛 𝚅𝚎𝚛𝚒𝚂𝚘𝚗:** `{__version__}`
➠ **𝙿𝚛𝚘𝙶𝚛𝚊𝚖 𝚅𝚎𝚛𝚒𝚂𝚘𝚗:** `{pyro_vr}`
➠ **𝚙𝚈𝙳𝚎𝚟𝚒𝚕𝚔𝚒ñ𝚐 𝚅𝚎𝚛𝚒𝚂𝚘𝚗:** `{pip_vr}`
➠ **𝙲𝚑à𝙽𝚗𝙴𝚕:** @SaNkiFigHter1
━───────╮•╭───────━
➠ **Source Code:** [•𝙴𝚗𝚓𝙾𝚢😈•](https://te.legra.ph/file/1facd8b18af633fa20eaa.mp4)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
