import asyncio
from scrapli.driver.core import AsyncIOSXEDriver
from scrapli import Scrapli
from datetime import datetime
from pathlib import Path
from devices import DEVICES
from commands import COMMANDS
import logging


SUCCESS = 55
logging.addLevelName(SUCCESS , 'SUCCESS')

logging.basicConfig(
    filename="process-logging.log",
    filemode="a",
    format="%(asctime)s:%(name)s - %(message)s",
    datefmt= "%d-%m-%Y %H:%M:%S",
    level=logging.ERROR)

logger=logging.getLogger()


today = datetime.today().date()


async def collect_commands(hostname, device):
    conn = AsyncIOSXEDriver(**device)
    try:
        await conn.open()
    except Exception as error:
        logger.error(f"ERROR: {hostname} - Failed to connect device\n{error}")
    else:
        config_dir = f"archive/{today}/{hostname}"
        Path(config_dir).mkdir(parents=True, exist_ok=True)
        for feature,commands in COMMANDS.items():
            response = await conn.send_commands(commands, strip_prompt=False)
            if response.failed:
                logger.error(f"ERROR: {hostname} - Failed to get command(s)\n{response.result}")
            else:
                filename = f"{config_dir}/{feature}.txt"
                with open(filename, "w") as file:
                    file.write(response.result)
                    file.close()
                logger.log(SUCCESS, f"SUCCESS: {hostname} - Commands collected.\n{commands}")

        await conn.close()


async def main():
    coroutines = [collect_commands(hostname, device) for hostname, device in DEVICES.items()]
    results = await asyncio.gather(*coroutines)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())