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
๐ฐ Speed : {3}/s\n\n
๐ Done : {1}\n\n
๐ฅ Total size  : {2}\n\n
โณ Time left : {4}\n\n
"""
    ID_TEXT = """
๐ Your Telegram ID โ <code>{}</code>
"""

    INFO_TEXT = """

 ๐คน First Name : <b>{}</b>

 ๐ดโโ๏ธ Second Name : <b>{}</b>

 ๐ง๐ปโ๐ Username : <b>@{}</b>

 ๐ Telegram Id : <code>{}</code>

 ๐ Profile Link : <b>{}</b>

 ๐ก Dc : <b>{}</b>

 ๐ Language : <b>{}</b>

 ๐ฒ Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('โ Help', callback_data='help'),
            InlineKeyboardButton('๐ About', callback_data='about')
        ], [
            InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('๐  Home', callback_data='home'),
            InlineKeyboardButton('๐ About', callback_data='about')
        ], [
            InlineKeyboardButton('โ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('๐  Home', callback_data='home'),
            InlineKeyboardButton('โ Help', callback_data='help')
        ], [
            InlineKeyboardButton('โ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('โ Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats below."
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Trying to Download โ\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n๐ค Uploading Please Wait "
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\n\nUploaded in {} seconds"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "โ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process Free users only 1 request per 4 hrs\n
Upgrade your /plans to Remove Time Gaps and For link Processing"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL."
