import asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import MONGO_DB_URI
print("[INFO]: STARTING MONGO DB CLIENT")
mongo_client = MongoClient(MONGO_DB_URI)
mondb =  "mongodb+srv://hevc:sucks@cluster0.mdnim6a.mongodb.net/?retryWrites=true&w=majority"
mongo_clientx = MongoClient(mondb)
db = mongo_client.autoanime
dbx = mongo_clientx["techzcloud"]
filesdb = dbx["files"]
animedb = db.animes
uploadsdb = db.uploads
user_data = db['users']

async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def get_animesdb(): 
    anime_list = []
    async for name in animedb.find():
        anime_list.append(name)
    return anime_list

async def save_animedb(name,data): 
    data = await animedb.insert_one({"name": name, "data": data})
    return
  
async def del_anime(name): 
    data = await animedb.delete_one({"name": name})
    return

async def get_uploads(): 
    anime_list = []
    async for name in uploadsdb.find():
        anime_list.append(name)
    return anime_list

async def save_uploads(name): 
    data = await uploadsdb.insert_one({"name": name})
    return

def is_fid_in_db(fid):
    data = filesdb.find_one({"fid": fid})
    if data:
        return data
    else:
        return None
