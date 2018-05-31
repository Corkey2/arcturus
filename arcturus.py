#Arcturus by Harry Evett

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from random import randint

bot = commands.Bot(command_prefix = '=')

@bot.event
async def on_ready():
    print('{} at your service!'.format(bot.user.name))

@bot.command(pass_context=True)
async def praise(ctx):
    choice = randint(1,8)
    praise_type = randint(1,3)
    if choice == 1:
        yter = 'Harry Evett'
    if choice == 2:
        yter = 'JG Science'
    if choice == 3:
        yter = 'Times Infinity'
    if choice == 4:
        yter = 'Reigarw'
    if choice == 5:
        yter = 'Vsauce'
    if choice == 6:
        yter = 'Veritasium'
    if choice == 7:
        yter = 'Dreksler'
    if choice == 8:
        yter = 'Kurzgesagt'
    if praise_type == 1:
        await bot.say("Isn't {} the best youtuber ever?".format(yter))
    if praise_type == 2:
        await bot.say("Everybody loves {}.".format(yter))
    if praise_type == 3:
        await bot.say("Subscribe to {}!".format(yter))

@bot.command(pass_context=True)
async def about(ctx, user: discord.Member):
    await bot.say('User name: {}'.format(user.name))
    await bot.say('User ID: {}'.format(user.id))
    await bot.say('User status: {}'.format(user.status))
    await bot.say('User highest role: {}'.format(user.top_role))
    await bot.say('Date joined: {}'.format(user.joined_at))
    
    
    
    print('Praise successful')

bot.run('NDUxODMyODA1NTM4NzkxNDI0.DfHxIg.veNDJqKuXAexh0J1DW2EIFMorvk')
