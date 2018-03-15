#!/usr/bin/env python
from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.types import Channel

from config import API_ID, API_HASH

client = TelegramClient('experimental_client', API_ID, API_HASH)
client.start()

dialogs = client.get_dialogs()

for dialog in dialogs:
    if type(dialog.entity) is Channel:
        print(dialog.name)
        client(LeaveChannelRequest(dialog.entity))
