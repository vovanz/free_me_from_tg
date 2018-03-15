#!/usr/bin/env python
from telethon import TelegramClient

from config import API_ID, API_HASH

client = TelegramClient('experimental_client', API_ID, API_HASH)
client.start()
