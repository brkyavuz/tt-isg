from scrapli.driver.core import AsyncIOSXEDriver
from os import environ
from dotenv import load_dotenv

load_dotenv()
auth_username = environ.get('DEVICE_USER')
auth_password = environ.get('DEVICE_PASS')

DEVICES ={
        "ANK-CORE-ISG-01-1": {
            "host": "10.139.66.19",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        "ANK-CORE-ISG-01-2": {
            "host": "10.139.66.20",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        "ANK-CORE-ISG-02-1": {
            "host": "10.139.66.21",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        "ANK-CORE-ISG-02-2": {
            "host": "10.139.66.22",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        "IST-CORE-ISG-01-1": {
            "host": "10.139.67.19",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        "IST-CORE-ISG-01-2": {
            "host": "10.139.67.20",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        "IST-CORE-ISG-02-1": {
            "host": "10.139.67.21",
            "auth_username": auth_username,
            "auth_password": auth_password,
            "auth_strict_key": False,
            "transport": "asyncssh",
            },
        }