"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26376042")
    API_HASH  = os.environ.get("API_HASH", "1f5343b0646645ca1eaf7c4759fc248f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7012541014:AAFI2an6FRSqyZSYrXqyHuxYxSYeNNgNBiU") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Zenitsuaf:Zenitsuaf@cluster0.i58aapw.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/3ebcefec1b1f0b95f7759.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5817124748').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "0") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001586987735"))   
    FILES_CHANNEL = int(os.environ.get("FILES_CHANNEL", "-1001586987735"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {}

⚡ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 Zenith 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐑𝐄𝐍𝐀𝐌𝐄 𝐁𝐎𝐓! ⚡

➝  Introducing Advanced Rename Bot – your ultimate solution for effortless file renaming, featuring customizable captions, thumbnails, and seamless sequencing.
────────────────────
✨ Tʜɪs Bᴏᴛ ɪs Cʀᴇᴀᴛᴇᴅ ʙʏ <a href='https://t.me/NINJA_OBITO_SAI'>OBITO</a>
────────────────────
➝  For assistance or more How to use me, use the " /Tutorial "command or you can use the below "Support" button to contact us.

‼️ Explore my commands by clicking on the "⚡ Commands ⚡" button to use me more precisely " ‼️

🚀 𝐋𝐄𝐓'𝐒 𝐆𝐄𝐓 𝐒𝐓𝐀𝐑𝐓𝐄𝐃! 🚀"""
    
    FILE_NAME_TXT = """
    <u><b>SETUP AUTO RENAME FORMAT</b></u>\n\nUse These Keywords To Setup Custom File Name\n\n➝ episode :- to replace episode number\n➝ quality :- to replace video resolution\n\n‣ <b>Example :</b> /autorename [AX] S02 - EPepisode Spy X Family [quality] [Sub] @Animes_XYZ.mkv\n\n‣ <b>Your Current Rename Format :</b> {format_template}
    """
    
    ABOUT_TXT = f"""
<b>╔════════════⦿
├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={6748415360}'>⚚ NINJA OBITO SAI </a>
├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>
├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
├⋗ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/NINJA_OBITO_SAI'>Click Here</a>
├⋗ Main Channel : <a href='https://t.me/smiley_bots'>Anime Channel</a>
├⋗ Support Group : <a href='https://t.me/smileybotz_group'>Group Chat</a>
╚═════════════════⦿</b>
"""

    
    THUMB_TXT = """ just send the image nigga"""

    PREMIUM_TXT = """free
    
    give tg Prem to @sexy_slayer 🙂"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    COMMANDS_TXT = """<b><u>/format - ifykyk </b></u>
    """

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


