#! /bin/env python3

from dotenv import load_dotenv
import discord
import os

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello {0}!'.format(message.author.name))


@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        msg = f'Hi {member.name}!\nWelcome to {guild.name}'
        await guild.system_channel.send(msg)

client.run(os.getenv('TOKEN'))
