#!/usr/bin/python3
import time, random, traceback, os, json, datetime, discord, logging, asyncio
from credentials import *

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='maia.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class Maia(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    async def on_message(self, message):
        # Verifies the bot ignores messages sent BY the bot.
        if message.author.id == self.user.id:
            return
        
        # Responds to the message "!test" with data about the message
        if message.content.startswith('!test'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            await message.channel.send('Message Author: {0.author}'.format(message))
            await message.channel.send('Message Content: {0.content}'.format(message))

client = Maia()
client.run(Token)

