import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "736532225-w") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Yato")     
    DB_URL  = os.environ.get("DB_URL","mongodb")
    PORT = os.environ.get("PORT", "8280")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/29a3acbbab9de5f45a5fe.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6497757690').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'codeflix_bots').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001868871195"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1001868871195"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # Part of text configuration
    START_TXT = """<b>👋 Hey there, {}

📁 I'm your advanced rename bot—built to transform your files with flair:
• Auto-renaming with custom captions
• Thumbnail embedding for visual punch
• Seamless sequencing for perfect order</b>"""


<b>Variables :</b>
➲ Episode - to replace episode number  
➲ Season - to replace season number  
➲ Quality - to replace quality  

<b>‣ For ex:- </b> `/autorename Overflow [Season Episode] - [Dual] quality`

<b>‣ /Autorename: Rename your media files by including 'episode' and 'quality' variables in your text, to extract episode and quality present in the original filename."""
    
    ABOUT_TXT = f"""<b>❍ My name : <a href="https://t.me/xspes">Auto Rename</a>
❍ Developer : <a href="https://t.me/cosmic_freak">Yato</a>
❍ Github : <a href="https://github.com/cosmic_freak">Yato</a>
❍ Language : <a href="https://www.python.org/">Python</a>
❍ Database : <a href="https://www.mongodb.com/">Mongo DB</a>
❍ Hosted on : <a href="https://t.me/xspes">VPS</a>
❍ Main channel : <a href="https://t.me/modstorexd">Mods Store</a>

➻ Click on the buttons given below for getting basic help and info about me.</b>"""

    
    THUMBNAIL_TXT = """<b><u>» To set custom thumbnail</u></b>
    
➲ /start: Send any photo to automatically set it as a thumbnail..
➲ /del_thumb: Use this command to delete your old thumbnail.
➲ /view_thumb: Use this command to view your current thumbnail.

Note: If no thumbnail saved in bot then, it will use thumbnail of the original file to set in renamed file"""

    CAPTION_TXT = """<b><u>» To set custom caption and media type</u></b>
    
<b>Variables :</b>         
Size: {filesize}
Duration: {duration}
Filename: {filename}

➲ /set_caption: To set a custom caption.
➲ /see_caption: To view your custom caption.
➲ /del_caption: To delete your custom caption.

» For ex:- /set_caption File name: {filename}"""

    PROGRESS_BAR = """\n
<b>» Size</b> : {1} | {2}
<b>» Done</b> : {0}%
<b>» Speed</b> : {3}/s
<b>» ETA</b> : {4} """
    
    
    DONATE_TXT = """<blockquote> Thanks for showing interest in donation</blockquote>

<b><i>💞 If you like our bot feel free to donate any amount ₹10, ₹20, ₹50, ₹100, etc.</i></b>

Donations are really appreciated it helps in bot development

 <u>You can also donate through UPI</u>

 UPI ID : <code>LodaLassan@fam</code>

If you wish you can send us ss
on - @xspes"""

    PREMIUM_TXT = """<b>Upgrade to our premium service and enjoy exclusive features:
○ Unlimited Renaming: Rename as many files as you want without any restrictions.
○ Early Access: Be the first to test and use our latest features before anyone else.

• Use /plan to see all our plans at once.

➲ First step : Pay the amount according to your favorite plan to this rohit162@fam UPI ID.

➲ Second step : Take a screenshot of your payment and share it directly here: @xspes

➲ Alternative step : Or upload the screenshot here and reply with the /bought command.

Your premium plan will be activated after verification</b>"""

    PREPLANS_TXT = """<b>👋 Hai,
    
🎖️ <u>Available plans</u> :

Pricing:
➜ Monthly premium: ₹50/month
➜ Daily premium: ₹5/day
➜ For bot hosting: contact @xspes

➲ UPI ID - <code>LodaLassan@fam</code>

‼️Upload the payment screenshot here and reply with the /bought command.</b>"""
    
    HELP_TXT = """<b>Here is help menu important commands:

Awesome features🫧

Rename bot is a handy tool that helps you rename and manage your files effortlessly.

➲ /Autorename: Auto rename your files.
➲ /Metadata: Commands to turn on off metadata.
➲ /Help: Get quick assistance.</b>"""

    SEND_METADATA = """
<b>--Metadata Settings:--</b>

➜ /metadata: Turn on or off metadata.

<b>Description</b> : Metadata will change MKV video files including all audio, streams, and subtitle titles."""


    SOURCE_TXT = """
<b>Hey,
 This is auto rename bot,
An open source telegram auto rename bot.</b>

Written in python with the help of :
[Pyrogram](https://github.com/pyrogram/pyrogram)
[Python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
And using [Mongo](https://cloud.mongodb.com) as database.


<b>Here is my source code :</b> [Github](https://github.com/codeflix_bots/autorenamebot)


Auto rename bot is licensed under the [MIT license](https://github.com/codeflix_bots/autorenamebot/blob/main/LICENSE).
© 2024 | [Support chat](https://t.me/codeflixsupport), all rights reserved."""

    META_TXT = """
**Managing metadata for your videos and files**

**Various metadata:**

- **Title**: Descriptive title of the media.
- **Author**: The creator or owner of the media.
- **Artist**: The artist associated with the media.
- **Audio**: Title or description of audio content.
- **Subtitle**: Title of subtitle content.
- **Video**: Title or description of video content.

**Commands to turn on off metadata:**
➜ /metadata: Turn on or off metadata.

**Commands to set metadata:**

➜ /settitle: Set a custom title of media.
➜ /setauthor: Set the author.
➜ /setartist: Set the artist.
➜ /setaudio: Set audio title.
➜ /setsubtitle: Set subtitle title.
➜ /setvideo: Set video title.

**Example:** /settitle Your Title Here

**Use these commands to enrich your media with additional metadata information!**


