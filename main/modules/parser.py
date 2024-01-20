import asyncio
from main.modules.utils import status_text
from main import status
from main.modules.db import get_animesdb, get_uploads, save_animedb
import feedparser
from main import queue
from main.inline import button1

def trim_title(title: str):
    title = title.replace("[Erai-raws] ", "")
    title = title.replace("Dr. Stone - New World Cour 2", "Dr Stone New World Part 2")
    title = title.replace("Mahou Tsukai no Yome Season 2 Cour 2", "Mahou Tsukai no Yome Season 2 Part 2")
    title = title.replace("Dead Mount Death Play 2nd Cour", "Dead Mount Death Play Part 2")
    title = title.replace("Shangri-La Frontier - Kusogee Hunter, Kamige ni Idoman to Su", "Shangri-La Frontier")
    title = title.replace("Hataraku Maou-sama!! Part 2", "The Devil is a Part-Timer! S2 Part 2")
    title = title.replace("Tian Guan Ci Fu Di Er Ji", "Heaven Official's Blessing S2")
    title = title.replace("Solo Leveling S01E02 If I Had One More Chance 1080p AMZN WEB-DL DDP2.0 H 264-VARYG (Ore dake Level Up na Ken, Multi-Subs)", "Solo Leveling - 02")
    title = "Solo Leveling - 03"
    ext = ".mkv"
    title = title + ext
    return title

def multi_sub(title: str):
    subtitle = "English, Chinese, Indonesian, Thai, Vietnamese" 
    return subtitle

def parse():
    a = feedparser.parse("https://nyaa.si/?page=rss&u=varyg1001&q=solo%20leveling")
    b = a["entries"]
    b = b[0:1]
    data = []    

    for i in b:
        item = {}
        item['title'] = trim_title(i['title'])
        item['size'] = '1.1 GiB' 
        item['link'] = "magnet:?xt=urn:btih:4e0a5bd60202132ec14e883a68b5ffd4fd3cff5b"
        data.append(item)
    data.reverse()
    return data

async def auto_parser():
    while True:
        try:
            await status.edit(await status_text("Parsing Rss, Fetching Magnet Links..."),reply_markup=button1)
        except:
            pass

        rss = parse()
        data = await get_animesdb()
        uploaded = await get_uploads()

        saved_anime = []
        for i in data:
            saved_anime.append(i["name"])

        uanimes = []
        for i in uploaded:
            uanimes.append(i["name"])
        
        for i in rss:
            if i["title"] not in uanimes and i["title"] not in saved_anime:
                if ".mkv" in i["title"] or ".mp4" in i["title"]:
                    title = i["title"]
                    await save_animedb(title,i)

        data = await get_animesdb()
        for i in data:
            if i["data"] not in queue:
                queue.append(i["data"])    
                print("Saved ", i["name"])   

        try:
            await status.edit(await status_text("Idle..."),reply_markup=button1)
            await asyncio.sleep(5)
        except:
            pass

        await asyncio.sleep(60)
