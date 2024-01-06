import asyncio

import os

import time

import pixeldrain

import aiohttp

import requests

import aiofiles

from main.modules.utils import format_time, get_duration, get_epnum, get_filesize, status_text, tags_generator, get_messages, b64_to_str, str_to_b64, send_media_and_reply, get_durationx

from main.modules.anilist import get_anime_name

from main.modules.anilist import get_anime_img

from main.modules.db import present_user, add_user, is_fid_in_db

from main.modules.thumbnail import generate_thumbnail

from config import UPLOADS_ID

from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from main.modules.progress import progress_for_pyrogram

from os.path import isfile

import os

import time

from main import app, status

from pyrogram.errors import FloodWait

from main.inline import button1

async def upload_video(msg: Message,file,id,tit,name,ttl,sourcetext,untext,subtitle,nyaasize,thumbnail):

    try:

        fuk = isfile(file)

        if fuk:

            r = msg

            c_time = time.time()

            duration = get_duration(file)

            durationx = get_durationx(file)

            size = get_filesize(file)

            ep_num = get_epnum(name)

            rest = tit


            filed = os.path.basename(file)

            filed = filed.replace("[1080p Web-DL]", "[720p x265] @animxt")

            fukpath = "downloads/" + filed

            caption = f"{filed}"

            caption = caption.replace("[720p x265] @animxt.mkv", "") 

            gcaption=f"**{caption}**" + "\n" +  f"__({tit})__" + "\n" + "━━━━━━━━━━━━━━━━━━━" + "\n" + "✓  `720p x265 10Bit`" + "\n" + f"✓  `{subtitle} ~ Subs`" + "\n" + "#Encoded #HEVC"

            kayo_id = -1001642923224

            gay_id = 1159872623

            x = await app.send_document(

                kayo_id,

            document=file,

            caption=gcaption,

            file_name=filed,

            force_document=True,     

            thumb=thumbnail

            )

            os.rename(file,fukpath)
            
 
            fid = str(x.message_id)
            da_url = "https://da.gd/"
            teleshare = f"https://telegram.me/somayukibot?start=animxt_{str_to_b64(fid)}"
        
            await asyncio.sleep(10)
            id = await is_fid_in_db(fid) 
            if id:
                hash = id["code"]
                ddl = f"https://ddl.animxt.fun/beta/{hash}"
            api_url = f"https://nanolinks.in/api?api=7da8202d8af0c8d76c024a6be6badadaabe66a01&url={ddlx}&format=text"
            print(ddl)
            result = requests.get(api_url)
            nai_text = result.text
   
            url = nai_text
            shorten_url = f"{da_url}shorten"
            response = requests.post(shorten_url, params={"url": url})
            nyaa_text = response.text.strip()
            repl_markup=InlineKeyboardMarkup(

                [

                    [

                         InlineKeyboardButton(

                            text="🐌TG FILE",

                            url=teleshare

                        ),

                         InlineKeyboardButton(

                              text="🚀BETA DL",

                              url=nyaa_text,

                        ),
  
                    ],
                    
                ],
            )

            encodetext =  f"{sourcetext}" "\n" + f"**‣ File Size**: `{size}`" + "\n" + f"**‣ Duration**: {durationx}" + "\n" + f"**‣ Downloads**: [🔗Telegram File]({teleshare}) [🔗BETA DL]({nyaa_text})"

            await asyncio.sleep(5)

            entext = await untext.edit(encodetext, disable_web_page_preview=True, reply_markup=repl_markup)

    except Exception:

            await app.send_message(kayo_id, text="Something Went Wrong!")

    try:
        
            
            await r.delete()

            os.remove(file)

            os.remove(thumbnail)

    except:

        pass

    return x.message_id
