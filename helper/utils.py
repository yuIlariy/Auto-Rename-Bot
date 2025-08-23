import math, time
from datetime import datetime
from pytz import timezone
from config import Config, Txt 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import re
import random


# Speed icon selector
def get_speed_icon(speed_bps):
    speed_mbps = speed_bps / (1024 * 1024)
    if speed_mbps < 7:
        return "🐢"
    elif speed_mbps < 11:
        return "🚀"
    else:
        return "🛸"

# Footer variants
THEMED_FOOTERS = {
    "🐢": [
        "╰━🐢 Slow & steady wins the rename ━➣",
        "╰━🧘 Patience is a patching virtue ━➣",
        "╰━📦 Unboxing at turtle speed ━➣",
        "╰━🌿 Rename growing organically ━➣",
        "╰━🪴 Gentle patching in progress ━➣",
        "╰━🧊 Rename chilling in low gear ━➣",
        "╰━🐌 Sluggish but steady ━➣",
        "╰━🧵 Threading bytes with care ━➣",
        "╰━🪙 Rename crawling byte by byte ━➣",
        "╰━🧺 Slow basket of bits ━➣",
        "╰━🪶 Rename floating softly ━➣",
        "╰━🧸 Cozy patching underway ━➣",
        "╰━🕯️ Rename lit by patience ━➣",
        "╰━🫧 Bubble-speed rename ━➣",
        "╰━🧂 Lightly seasoned rename ━➣",
        "╰━🧃 Rename sipping bandwidth ━➣",
        "╰━🫖 Rename brewing slowly ━➣",
        "╰━🧺 Basket of bytes unfolding ━➣",
        "╰━🧦 Rename wrapped in comfort ━➣",
        "╰━🧘‍♂️ Zen rename in motion ━➣"
    ],
    "🚀": [
        "╰━🚀 Rename rocket in motion ━➣",
        "╰━⚡ Fast patch, clean finish ━➣",
        "╰━🎯 Target acquired, speed locked ━➣",
        "╰━🧩 Modular rename at warp speed ━➣",
        "╰━💨 Rename breezing through ━➣",
        "╰━🛠️ Precision patching active ━➣",
        "╰━📡 Rename pinged and patched ━➣",
        "╰━🧪 Rename chemistry optimized ━➣",
        "╰━📈 Rename trending upward ━➣",
        "╰━🧭 Rename locked on course ━➣",
        "╰━🧰 Rename toolkit deployed ━➣",
        "╰━🎮 Rename in turbo mode ━➣",
        "╰━🧠 Rename thinking fast ━➣",
        "╰━🧤 Rename gripping bytes ━➣",
        "╰━🧱 Rename stacking clean ━➣",
        "╰━🧼 Rename polished mid-flight ━➣",
        "╰━🧯 Rename fireproofed ━➣",
        "╰━🧞 Rename granting speed wishes ━➣",
        "╰━🧃 Rename juiced up ━➣",
        "╰━🧳 Rename packed and moving ━➣"
    ],
    "🛸": [
        "╰━🛸 Rename from another dimension ━➣",
        "╰━🌌 Ultra-speed patching engaged ━➣",
        "╰━🧬 Quantum rename sequence ━➣",
        "╰━💫 Rename transcending limits ━➣",
        "╰━🪐 Rename orbiting perfection ━➣",
        "╰━🧠 Rename outsmarting gravity ━➣",
        "╰━🧿 Rename seeing beyond bytes ━➣",
        "╰━🧲 Rename magnetized for speed ━➣",
        "╰━🧪 Rename formula unlocked ━➣",
        "╰━🧱 Rename warping structure ━➣",
        "╰━🧞‍♂️ Rename summoned from hyperspace ━➣",
        "╰━🧤 Rename gripping galaxies ━➣",
        "╰━🧰 Rename toolkit from the future ━➣",
        "╰━🧭 Rename navigating wormholes ━➣",
        "╰━🧼 Rename polished by stardust ━➣",
        "╰━🧯 Rename fireproofed at light speed ━➣",
        "╰━🧃 Rename juiced with cosmic energy ━➣",
        "╰━🧳 Rename packed for interstellar travel ━➣",
        "╰━🧩 Rename solving galactic puzzles ━➣",
        "╰━🧠 Rename thinking faster than light ━➣"
    ]
}

# Main progress function
async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        speed_icon = get_speed_icon(speed)

        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress_bar = "{0}{1}".format(
            ''.join(["▣" for _ in range(math.floor(percentage / 5))]),
            ''.join(["▢" for _ in range(20 - math.floor(percentage / 5))])
        )

        footer = random.choice(THEMED_FOOTERS.get(speed_icon, ["╰━━━━━━━━━━━━━━━━➣"]))

        progress_template = f"""<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣

┃    🗂️ ᴄᴏᴍᴘʟᴇᴛᴇᴅ: {humanbytes(current)}

┃    📦 ᴛᴏᴛᴀʟ ꜱɪᴢᴇ: {humanbytes(total)}

┃    🔋 ꜱᴛᴀᴛᴜꜱ: {round(percentage, 2)}%

┃    {speed_icon} ꜱᴘᴇᴇᴅ: {humanbytes(speed)}/s

┃    ⏰ ᴇᴛᴀ: {estimated_total_time}

{footer}
</b>"""

        tmp = progress_bar + progress_template

        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲ᴇʟ ✖️", callback_data="close")]]
                )
            )
        except:
            pass


def humanbytes(size):    
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'ʙ'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "ᴅ, ") if days else "") + \
        ((str(hours) + "ʜ, ") if hours else "") + \
        ((str(minutes) + "ᴍ, ") if minutes else "") + \
        ((str(seconds) + "ꜱ, ") if seconds else "") + \
        ((str(milliseconds) + "ᴍꜱ, ") if milliseconds else "")
    return tmp[:-2] 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

async def send_log(b, u):
    if Config.LOG_CHANNEL is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            Config.LOG_CHANNEL,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {u.mention}\nIᴅ: `{u.id}`\nUɴ: @{u.username}\n\nDᴀᴛᴇ: {date}\nTɪᴍᴇ: {time}\n\nBy: {b.mention}"
        )

def add_prefix_suffix(input_string, prefix='', suffix=''):
    pattern = r'(?P<filename>.*?)(\.\w+)?$'
    match = re.search(pattern, input_string)
    if match:
        filename = match.group('filename')
        extension = match.group(2) or ''
        if prefix == None:
            if suffix == None:
                return f"{filename}{extension}"
            return f"{filename} {suffix}{extension}"
        elif suffix == None:
            if prefix == None:
               return f"{filename}{extension}"
            return f"{prefix}{filename}{extension}"
        else:
            return f"{prefix}{filename} {suffix}{extension}"


    else:
        return input_string
