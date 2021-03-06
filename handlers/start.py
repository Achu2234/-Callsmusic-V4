import os

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2


## ~ Simple Config ~ ##
FRIEND_BOT = "MusicsNexa_bot"
USER_ACCNAME = os.getenv("USER_ACCNAME", "NexaMusicAssistant")



@Client.on_message(command(["start", "start@TheNexasMusic_bot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ๐๏ธ!</b>

I'm The Nexa Music Bot. Friend of **@{FRIEND_BOT}** ๐๏ธ.

I can play Music In Telegram Groups Via Voice Chat! ๐๏ธ.

Made with โค๏ธ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐คจ๏ธ How To Use Me ๐คจ๏ธ", url="https://telegra.ph/How-To-Use-Music-Nexa-Bot-03-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ฐ๏ธ My Update Channel ๐ฐ๏ธ", url="https://t.me/NexaBotsUpdates"
                    ),
                    InlineKeyboardButton(
                        "โ๏ธ Support Group โ๏ธ", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(command(["help", "help@TheNexasMusic_bot"]))
async def help(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ๐๏ธ!</b>

Bruh! Do you need Help! ๐ค๏ธ yea yea I know it! ๐๏ธ

How To Use Me? ๐ง๏ธ

<b> 1. Add Me and @{USER_ACCNAME} To Your Group!

 2. Give Admin To Me and @{USER_ACCNAME} ! </b>
 
 Enjoy! ๐๏ธ

Made with โค๏ธ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฐ๏ธ My Update Channel ๐ฐ๏ธ", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ๏ธ Support Group โ๏ธ", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["cmdlist", "cmdlist@TheNexasMusic_bot"]))
async def cmdlist(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ๐๏ธ!</b>

Here is the list of available commands! ๐๏ธ

<code>/play</code> - Reply to supported url or "/play supported url"
<code>/skip</code> - Skip currenly playing song!
<code>/pause</code> - Pause currently playing song!
<code>/resume</code> - Resume currently pushed song!
<code>/mute</code> - Mutes Streamer!
<code>/unmute</code> - Unmutes streamer!
<code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
<code>/yts (song name)</code> - Download song by it's name!
 
 Enjoy! ๐๏ธ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๏ธ Supported Sites ๐๏ธ", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ๏ธ Support Group โ๏ธ", url="https://t.me/Nexa_bots"
                    )
                ],
                [
                    InlineKeyboardButton(
                    "๐ฐ๏ธ My Update Channel ๐ฐ๏ธ", url="https://t.me/NexaBotsUpdates"
                    )
                ]
            ]
        )
    )
   
    
@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ๐๏ธ!</b>

__Note!__ โ?๏ธ: This Project Is <b>Not Fully Owned By Me</b> !

Credits To,

<b><a href="https://github.com/CallsMusic">CallsMusic</a></b> - For Callsmusic (Main Code โค๏ธ) !
<b><a href="https://github.com/nikhileashy">N A C</a></b> - For <code>/vc</code> Command

Made with โค๏ธ by **@NexaBotsUpdates**

Respect To Code Owners! Not To Me!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฐ๏ธ My Update Channel ๐ฐ๏ธ", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ๏ธ Support Group โ๏ธ", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )   


@Client.on_message(command(["vc", "vc@TheNexasMusic_bot"]) & other_filters)
async def vc(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ๐๏ธ!</b>


             ๐๏ธ  **Voice Chat Link** ๐๏ธ
____________________------------______________________

๐๏ธ https://t.me/{message.chat.username}?voicechat   ๐๏ธ
____________________------------______________________

Enjoy!๐๏ธโค๏ธ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฐ๏ธ My Update Channel ๐ฐ๏ธ", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ๏ธ Support Group โ๏ธ", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["search", "search@TheNexasMusic_bot"]))
async def search(_, message: Message):
    await message.reply_text(
        "๐๐ปโโ๏ธ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ Yeah", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Nope โ", callback_data="close"
                    )
                ]
            ]
        )
    )
