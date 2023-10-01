import asyncio
import logging
import aiohttp
import traceback
from .config import APP_URL
async def ping_server():
        sleep_time = 15
        while True:
            await asyncio.sleep(sleep_time)
            try:
                async with aiohttp.ClientSession(
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as session:
                    async with session.get(APP_URL) as resp:
                        logging.info("Pinged server with response: {}".format(resp.status))
            except TimeoutError:
                logging.warning("Couldn't connect to the site URL..!")
            except Exception:
                traceback.print_exc()
