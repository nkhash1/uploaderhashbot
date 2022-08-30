from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
Hi {} 

I am Url uploader bot.
 
"""

    HELP_TEXT = """

Send direct links and see magic.
 
"""


    ABOUT_TEXT = """

Bot to remotely upload files to telegram.

"""

    PROGRESS = """
🔰 Speed : {3}/s\n\n
🌀 Done : {1}\n\n
🎥 Total size  : {2}\n\n
⏳ Time left : {4}\n\n
"""
    ID_TEXT = """
🆔 Your Telegram ID → <code>{}</code>
"""

    INFO_TEXT = """

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ Help', callback_data='help'),
            InlineKeyboardButton('🎃 About', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Home', callback_data='home'),
            InlineKeyboardButton('🎃 About', callback_data='about')
        ], [
            InlineKeyboardButton('❎ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Home', callback_data='home'),
            InlineKeyboardButton('❓ Help', callback_data='help')
        ], [
            InlineKeyboardButton('❎ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❎ Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats below."
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Trying to Download ⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 Uploading Please Wait "
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\n\nUploaded in {} seconds"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process Free users only 1 request per 4 hrs\n
Upgrade your /plans to Remove Time Gaps and For link Processing"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL."
