import discord
from discord.ext import commands
from discord.ui import View, Button
from dotenv import load_dotenv
import os

import dotenv

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is running')
    await bot.change_presence(activity=discord.Game(name="Bjay's Bazaar"))

def admin_only():
    def predicate(ctx):
        return ctx.author.guild_permissions.administrator

    return commands.check(predicate)

####################################### welcome message #######################################
@bot.event
async def on_member_join(member):
    color_rgb = (0, 0, 0) 
    
    
    embed = discord.Embed(
        title=f"Welcome {member.mention} to Bjay's Bazaar!",
        description='Make sure to read <#1084586497270882385>!\nAlso check out <#1084584115342430288>, <#1139638659163893860> and <#1084584140432736258> to order!',
        color=discord.Color.from_rgb(*color_rgb)
    )
    
    embed.set_author(name="Bjay's Bazaar")
    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(embed=embed)

############################## MEMBER COUNT #################################################
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    await update_member_count(member.guild)

@bot.event
async def on_member_remove(member):
    await update_member_count(member.guild)

async def update_member_count(guild):
    channel = guild.get_channel(1139604335634944151)  # Replace with your channel ID
    if channel:
        member_count = len(guild.members)
        await channel.edit(name=f'👋丨{member_count}丨welcome')
      
################################ ALL ITEM EMBEDS ############################################
@bot.command()
@admin_only()
async def send_all_items(ctx):
    await send_embed_gear(ctx)
    await send_embed_pvp(ctx)
    await send_embed_blocks(ctx)
    await send_embed_food(ctx)
    await send_embed_misc(ctx)

################################# ALL KIT EMBEDS ############################################
@bot.command()
@admin_only()
async def send_all_kits(ctx):
    await send_starter(ctx)
    await send_travel(ctx)
    await send_pvp_kit(ctx)
    await send_regear(ctx)

####################################### PVP Kit #############################################
@bot.command()
@admin_only()
async def send_pvp_kit(ctx):
    color_rgb = (0, 0, 0)
    
    emoji_name = 'ingot'  
    emoji = discord.utils.get(ctx.guild.emojis, name=emoji_name)

    if emoji:
        
        embed = discord.Embed(
            title="PVP Kit",
            description=f"9 {emoji} / $1.50",
            color=discord.Color.from_rgb(*color_rgb)
        )
        embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')
        embed.set_image(url='https://i.postimg.cc/8PF7qCGV/pvpkit.png')

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Emoji {emoji_name} not found in the server!")

####################################### Starter Kit ##########################################
@bot.command()
@admin_only()
async def send_starter(ctx):
    color_rgb = (0, 0, 0)
    
    emoji_name = 'ingot'  
    emoji = discord.utils.get(ctx.guild.emojis, name=emoji_name)

    if emoji:
        
        embed = discord.Embed(
            title="Starter Kit",
            description=f"6 {emoji} / $1",
            color=discord.Color.from_rgb(*color_rgb)
        )
        embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')
        embed.set_image(url='https://i.postimg.cc/gkk8x4mG/starter-kit.png')

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Emoji {emoji_name} not found in the server!")

######################################## Travel Kit #########################################
@bot.command()
@admin_only()
async def send_travel(ctx):
    color_rgb = (0, 0, 0)
    
    emoji_name = 'ingot'  
    emoji = discord.utils.get(ctx.guild.emojis, name=emoji_name)

    if emoji:
        
        embed = discord.Embed(
            title="Travel Kit",
            description=f"6 {emoji} / $1",
            color=discord.Color.from_rgb(*color_rgb)
        )
        embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')
        embed.set_image(url='https://i.postimg.cc/tR86R62g/travelkit.png')

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Emoji {emoji_name} not found in the server!")

####################################### Regear Kit ############################################
@bot.command()
@admin_only()
async def send_regear(ctx):
    color_rgb = (0, 0, 0)
    
    emoji_name = 'ingot'  
    emoji = discord.utils.get(ctx.guild.emojis, name=emoji_name)

    if emoji:
        
        embed = discord.Embed(
            title="Regear Kit",
            description=f"9 {emoji} / $1.50",
            color=discord.Color.from_rgb(*color_rgb)
        )
        embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')
        embed.set_image(url='https://i.postimg.cc/8CJCFKyf/regearkit.png')

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Emoji {emoji_name} not found in the server!")
    
####################################### Rules ##############################################
@bot.command()
@admin_only()
async def send_embed_rules(ctx):
    color_rgb = (0, 0, 0)
    
    embed = discord.Embed(
        title="Rules",
        description="1. Do not spam in any form.\n\n2. Be respectful and civil.\n\n3. Do not ping without a legitimate reason.\n\nReact with :white_check_mark: to gain access to the server!",
        color=discord.Color.from_rgb(*color_rgb)
    )
    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)
##################################### ROLES ###################################################
@bot.command()
@admin_only()
async def send_embed_roles(ctx):
    color_rgb = (0, 0, 0)
    
    embed = discord.Embed(
        title="Shop Ping",
        description="React to this message if you want to get pinged whenever theres a giveaway or shop update.",
        color=discord.Color.from_rgb(*color_rgb)
    )
    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)
###################################### gear ###################################################
@bot.command()
@admin_only()
async def send_embed_gear(ctx):
    color_rgb = (0, 0, 0)
    server = bot.get_guild(1084583835724951713)
    ingot_emoji = discord.utils.get(server.emojis, name='ingot')

    if not ingot_emoji:
        ingot_emoji = ":x: Emoji not found: ingot"
  
    emoji_data = {
        'gset': f'= 2 {ingot_emoji}',
        'elytra': f'= 3 {ingot_emoji}',
        'gsword': f'= 1 {ingot_emoji}',
        'gpickaxe': f'= 0.5 {ingot_emoji}',
        'ghoe': f'= 0.5 {ingot_emoji}',
        'gshovel': f'= 0.5 {ingot_emoji}',
        'gaxe': f'= 0.5 {ingot_emoji}',
        'gbow': f'= 0.5 {ingot_emoji}', 
        'gcrossbow': f'= 0.5 {ingot_emoji}\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ',
         
    }

    emoji_strings = []

    for emoji_name, description in emoji_data.items():
        emoji = discord.utils.get(server.emojis, name=emoji_name)
        if emoji:
            emoji_strings.append(f"{str(emoji)} {description}")
        else:
            emoji_strings.append(f":x: Emoji not found: {emoji_name}")

    emoji_description = '\n\n'.join(emoji_strings)

    embed = discord.Embed(
        title='GEAR',
        description=emoji_description,
        color=discord.Color.from_rgb(*color_rgb)
    )

    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)

###################################### PVP ###################################################
@bot.command()
@admin_only()
async def send_embed_pvp(ctx):
    color_rgb = (0, 0, 0)
    server = bot.get_guild(1084583835724951713)
    ingot_emoji = discord.utils.get(server.emojis, name='ingot')
    stack_emoji = discord.utils.get(server.emojis, name='64')
    shulker_emoji = discord.utils.get(server.emojis, name='shulker')
    crystal_emoji = discord.utils.get(server.emojis, name='crystal')
  
    if not ingot_emoji:
        ingot_emoji = ":x: Emoji not found: ingot"

    if not stack_emoji:
        stack_emoji = ":x: Emoji not found: 64"

    if not shulker_emoji:
        stack_emoji = ":x: Emoji not found: shulker"

    emoji_data = {
        'crystal': f'{stack_emoji} = 1 {ingot_emoji}\n{str(crystal_emoji)} {shulker_emoji} = 18 {ingot_emoji}\n',
        'anchor': f'{stack_emoji} = 4 {ingot_emoji}\n',
        'pearl': f'{shulker_emoji} = 1 {ingot_emoji}\n',
        'totem': f'{shulker_emoji} = 0.5 {ingot_emoji}\n',
        'xp': f'{shulker_emoji} = 4 {ingot_emoji}\n',
        'speed': f'{shulker_emoji} = 0.25 {ingot_emoji}\n',
        'strength': f'{shulker_emoji} = 0.25 {ingot_emoji}\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ',
    }

    emoji_strings = []

    for emoji_name, description in emoji_data.items():
        emoji = discord.utils.get(server.emojis, name=emoji_name)
        if emoji:
            emoji_strings.append(f"{str(emoji)} {description}")
        else:
            emoji_strings.append(f":x: Emoji not found: {emoji_name}")

    emoji_description = '\n'.join(emoji_strings)

    embed = discord.Embed(
        title='PVP',
        description=emoji_description,
        color=discord.Color.from_rgb(*color_rgb)
    )

    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)

###################################### BLOCKS ###################################################
@bot.command()
@admin_only()
async def send_embed_blocks(ctx):
    color_rgb = (0, 0, 0)
    server = bot.get_guild(1084583835724951713)
    ingot_emoji = discord.utils.get(server.emojis, name='ingot')
    stack_emoji = discord.utils.get(server.emojis, name='64')
    shulker_emoji = discord.utils.get(server.emojis, name='shulker')
    gold_emoji = discord.utils.get(server.emojis, name='gold')
    iron_emoji = discord.utils.get(server.emojis, name='iron')
    redstone_emoji = discord.utils.get(server.emojis, name='redstone')
  
    if not ingot_emoji:
        ingot_emoji = ":x: Emoji not found: ingot"

    if not stack_emoji:
        stack_emoji = ":x: Emoji not found: 64"

    if not shulker_emoji:
        stack_emoji = ":x: Emoji not found: shulker"

    emoji_data = {
        'gold': f'{stack_emoji} = 1 {ingot_emoji}\n{str(gold_emoji)} {shulker_emoji} = 18 {ingot_emoji}\n',
        'iron': f'{stack_emoji} = 1 {ingot_emoji}\n{str(iron_emoji)} {shulker_emoji} = 12 {ingot_emoji}\n',
        'redstone': f'{stack_emoji} = 1 {ingot_emoji}\n{str(redstone_emoji)} {shulker_emoji} = 12 {ingot_emoji}\n',
        'emerald': f'{shulker_emoji} = 5 {ingot_emoji}\n',
        'bamboo': f'{shulker_emoji} = 0.5 {ingot_emoji}\n',
        'wool': f'{shulker_emoji} = 0.5 {ingot_emoji}\n',
        'glowstone': f'{shulker_emoji} = 3 {ingot_emoji}\n',
        'obsidian': f'{shulker_emoji} = 2 {ingot_emoji}\n',
        'echest': f'{stack_emoji} = 1 {ingot_emoji}\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ',
    }

    emoji_strings = []

    for emoji_name, description in emoji_data.items():
        emoji = discord.utils.get(server.emojis, name=emoji_name)
        if emoji:
            emoji_strings.append(f"{str(emoji)} {description}")
        else:
            emoji_strings.append(f":x: Emoji not found: {emoji_name}")

    emoji_description = '\n'.join(emoji_strings)

    embed = discord.Embed(
        title='BLOCKS',
        description=emoji_description,
        color=discord.Color.from_rgb(*color_rgb)
    )

    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)

####################################### FOOD ###################################################
@bot.command()
@admin_only()
async def send_embed_food(ctx):
    color_rgb = (0, 0, 0)
    server = bot.get_guild(1084583835724951713)
    ingot_emoji = discord.utils.get(server.emojis, name='ingot')
    stack_emoji = discord.utils.get(server.emojis, name='64')
    shulker_emoji = discord.utils.get(server.emojis, name='shulker')
    gapple_emoji = discord.utils.get(server.emojis, name='gapple')
  
    if not ingot_emoji:
        ingot_emoji = ":x: Emoji not found: ingot"

    if not stack_emoji:
        stack_emoji = ":x: Emoji not found: 64"

    if not shulker_emoji:
        stack_emoji = ":x: Emoji not found: shulker"

    emoji_data = {
        'gapple': f'{stack_emoji} = 1 {ingot_emoji}\n{str(gapple_emoji)} {shulker_emoji} = 18 {ingot_emoji}\n',
        'gcarrot': f'{shulker_emoji} = 1 {ingot_emoji}\n',
        'apple': f'{shulker_emoji} = 1 {ingot_emoji}\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ',
    }

    emoji_strings = []

    for emoji_name, description in emoji_data.items():
        emoji = discord.utils.get(server.emojis, name=emoji_name)
        if emoji:
            emoji_strings.append(f"{str(emoji)} {description}")
        else:
            emoji_strings.append(f":x: Emoji not found: {emoji_name}")

    emoji_description = '\n'.join(emoji_strings)

    embed = discord.Embed(
        title='FOOD',
        description=emoji_description,
        color=discord.Color.from_rgb(*color_rgb)
    )

    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)

####################################### MISC ###################################################
@bot.command()
@admin_only()
async def send_embed_misc(ctx):
    color_rgb = (0, 0, 0)
    server = bot.get_guild(1084583835724951713)
    ingot_emoji = discord.utils.get(server.emojis, name='ingot')
    stack_emoji = discord.utils.get(server.emojis, name='64')
    shulker_emoji = discord.utils.get(server.emojis, name='shulker')

    if not ingot_emoji:
        ingot_emoji = ":x: Emoji not found: ingot"
  
    emoji_data = {
        'tear': f'{shulker_emoji} = 2 {ingot_emoji}',
        'blaze_rod': f'{shulker_emoji} = 2 {ingot_emoji}',
        'gunpowder': f'{shulker_emoji} = 0.5 {ingot_emoji}',
        'rocket': f'{shulker_emoji} = 0.25 {ingot_emoji}',
        'sugarcane': f'{shulker_emoji} = 0.25 {ingot_emoji}',
        'stick': f'{shulker_emoji} = 0.25 {ingot_emoji}',
        'bottle': f'{shulker_emoji} = 0.5 {ingot_emoji}',
        'spider_eye': f'{shulker_emoji} = 0.5 {ingot_emoji}', 
        'witherskull': f'{shulker_emoji} = 20 {ingot_emoji}',
        'nametag': f'{stack_emoji} = 0.5 {ingot_emoji}\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ',
         
    }

    emoji_strings = []

    for emoji_name, description in emoji_data.items():
        emoji = discord.utils.get(server.emojis, name=emoji_name)
        if emoji:
            emoji_strings.append(f"{str(emoji)} {description}")
        else:
            emoji_strings.append(f":x: Emoji not found: {emoji_name}")

    emoji_description = '\n\n'.join(emoji_strings)

    embed = discord.Embed(
        title='MISCELLANEOUS',
        description=emoji_description,
        color=discord.Color.from_rgb(*color_rgb)
    )

    embed.set_thumbnail(url='https://i.postimg.cc/tT5qVKHk/bazaar.png')

    await ctx.send(embed=embed)


bot.run(token)