from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = "10471716"
API_HASH = getenv("f8a1b21a13af154596e2ff5bed164860")

BOT_TOKEN = getenv("7386576950:AAEHlgtmveuk8J4FY7p_uXi_9v_z0R_Dggk")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", "6883997969"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
