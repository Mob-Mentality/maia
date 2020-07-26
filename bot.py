#!/usr/bin/python3
import time, random, traceback, os, json, datetime, discord, logging, asyncio
from credentials import *
#Add Events Feature
import events

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='maia.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

varMessageLength = 0
varH1 = 0

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
            
            varMessageLength = len(message.content)
            varH1 = varH1 + varMessageLength
            
            await message.channel.send('Message tts: {0.tts}'.format(message))
            await message.channel.send('Message type: {0.type}'.format(message))
            await message.channel.send('Message author: {0.author}'.format(message))
            await message.channel.send('Message content: {0.content}'.format(message))
            await message.channel.send('Message length: {}'.format(varMessageLength))
            await message.channel.send('Message nonce: {0.nonce}'.format(message))
            await message.channel.send('Message embeds: {0.embeds}'.format(message))
            await message.channel.send('Message channel: {0.channel}'.format(message))
            await message.channel.send('Message mention_everyone: {0.mention_everyone}'.format(message))
            
        if message.content.startswith('!inventory'):
            
            print(varH1)
            await message.channel.send('H1: {}'.format(varH1)

        #Events commands
        if message.content.startswith('!events'):

            print('Events Command called')
            current_events()

client = Maia()
client.run(Token)
