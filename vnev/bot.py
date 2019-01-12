import asyncio as asyncio
import discord

import sekrets

client = discord.client.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print("bot logged in!")
    for s in client.get_server():
        print(s)

client.run(sekrets.TOKEN)
