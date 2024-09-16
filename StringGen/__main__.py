import asyncio
import importlib
from flask import Flask

from pyrogram import idle

from StringGen import LOGGER, Anony
from StringGen.modules import ALL_MODULES

# Flask app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)



async def anony_boot():
    try:
        await Anony.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringGen.modules." + all_module)

    LOGGER.info(f"@{Anony.username} Started.")
    await idle()


if __name__ == "__main__":
    Thread(target=run_flask).start()
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping String Gen Bot...")
