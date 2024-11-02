from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","23342470"))
API_HASH = getenv("API_HASH","824d7edf65f29a3bb7125173ff8ca9b0")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","6407861676"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://aradhyamusicbot:2QWdrmNlRVYovcVq@cluster0.ekjld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
