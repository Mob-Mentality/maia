#!/usr/bin/python3
import time, random, traceback, os, json, datetime, discord, logging, asyncio
from credentials import *
# Add Events Feature
import events

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='maia.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Initializing variables
varMessageLength = 0 # Used to store message length for later use.
varH1 = 5700 # Ansatz - Proton inventory
varH2 = 0 # Ansatz - Deuterium inventory
varAnsatzDelta = 0 # Ansatz - Used to store Ansatz material consumed

class Maia(discord.Client):

    # globalize variables
    global varMessageLength
    global varH1
    global varH2
    global varAnsatzDelta
    
    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    async def on_message(self, message):
        # Verifies the bot ignores messages sent BY the bot.
        if message.author.id == self.user.id:
            return
        
        #Ansatz Processing
        varMessageLength = len(message.content)
        varAnsatzDelta = varH1/20000
        
        if varAnsatzDelta < 1:
            varAnsatzDelta = 0
        
        varH1 = varH1 + varMessageLength - 2*varAnsatzDelta
        varH2 = varH2 + varAnsatzDelta
                    
        if message.content.startswith('!inventory'):
            
            print('H1: {}.format(varH1))
            print('H2: {}.format(varH2))
            await message.channel.send('H1: {}'.format(varH1))
            await message.channel.send('H2: {}'.format(varH2))
        
        # Responds to the message "!test" with data about the message
        if message.content.startswith('!test'):
            
            await message.channel.send('Message tts: {0.tts}'.format(message))
            await message.channel.send('Message type: {0.type}'.format(message))
            await message.channel.send('Message author: {0.author}'.format(message))
            await message.channel.send('Message content: {0.content}'.format(message))
            await message.channel.send('Message length: {}'.format(varMessageLength))
            await message.channel.send('Message nonce: {0.nonce}'.format(message))
            await message.channel.send('Message embeds: {0.embeds}'.format(message))
            await message.channel.send('Message channel: {0.channel}'.format(message))
            await message.channel.send('Message mention_everyone: {0.mention_everyone}'.format(message))

        # Events commands
        if message.content.startswith('!events'):

            print('Events Command called')
            current_events()

client = Maia()
client.run(Token)
