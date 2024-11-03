from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(10471716)
API_HASH = "f8a1b21a13af154596e2ff5bed164860"

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority"

OWNER_ID = int(getenv("OWNER_ID", 1356469075))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
