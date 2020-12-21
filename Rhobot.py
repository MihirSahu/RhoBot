import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

async def new(ctx, arg1, arg2):
    guild = ctx.message.guild
    if arg1 == "channel":
        await guild.create_text_channel(arg2)

    elif arg1 == "category":
        await ctx.guild.create_category(arg2)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if str(message.channel) == "rhobot-channel" and "addClass" in message.content:
        guild = message.guild
        msg = message.content
        role = discord.utils.get(guild.roles, name = "Mod") #create variable role and specify role
        #await guild.create_text_channel(msg[9:]) Create text channel
        await guild.create_category(msg[9:])
        await message.author.add_roles(role) #add role
        await message.channel.send("The category has been created and you can add channels to it now!")

    await client.process_commands(message)  #add this to the end of every event to make program look for commands as well. If you don't add commands won't work

"""
@client.command()
async def listCommands(message):

    if str(message.channel) == "rhobot-channel":
        await message.channel.send("testing")


@client.command()
async def help(message):

    if str(message.channel) == "rhobot-channel":
        await message.channel.send("testing")
"""

client.run('Token goes here')