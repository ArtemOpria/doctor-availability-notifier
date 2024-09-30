import time
import logging
import asyncio
import configparser
from telegram import Bot
from datetime import datetime
from functionality.driver import Driver
from functionality.parsing_helsi import HelsiSlots

# ——————————————— Logging settings ———————————————

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ——————————————— Telegram settings ———————————————

bot_token = config.get('Settings', 'bot_token', fallback='')
chat_id = config.get('Settings', 'chat_id', fallback='')
bot = Bot(token=bot_token)


# ——————————————— Page settings ———————————————

target_page = "https://helsi.me/doctor/ds_147"
exception_days = []

driver = Driver(target_page)
helsi_slots_instance = HelsiSlots.create_instance(driver)
helsi_slots_instance.exception_days.extend(exception_days)


# ——————————————— Main functionality ———————————————

async def send_message(message):
    try:
        await bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
    except Exception as e:
        logger.error(f"Error sending message: {e}")


async def main():
    try:
        while True:
            message_to_send = helsi_slots_instance.get_helsi_slots()
            if message_to_send:
                await asyncio.create_task(send_message(message_to_send))
            logger.info(f"Parsing helsi page... {datetime.now().strftime("%H:%M:%S")}")
            time.sleep(60)
            driver.refresh()
            time.sleep(3)
    except KeyboardInterrupt:
        pass
    finally:
        driver.close_page()


asyncio.run(main())
