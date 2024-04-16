"""
MIT License

Copyright (c) 2024 .Unknown.4.sure.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
os.system("pip install discord.py==1.7.3")
import json
import string
from typing import Any
import discord, aiohttp
from discord.ext import commands
import requests
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
from discord import Permissions
import requests
import time
from datetime import datetime, timedelta
from discord import Color, Embed, Member, embeds
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import smtplib
import re
import io
import webbrowser
import requests
from discord.utils import get
import pyfiglet
import random
import aiohttp
from googlesearch import search
os.system("pip install google")
import uuid
from bs4 import BeautifulSoup
from itertools import cycle
import psutil
import platform
#os.system("pip install PyNaCl")
import functools
from gtts import gTTS
from faker import Faker
import base64
import wolframalpha
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter

try:
    with open('config.json', 'r') as f:
        try:
            config = json.load(f)
            Duudu = config.get('Duudu')
            if not Duudu:
                raise ValueError("Token not found in config.json")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in config.json")
except FileNotFoundError:
    Duudu = input("Token: ")
except ValueError as e:
    print(f"Error: {e}")
    Duudu = input("Token: ")

colorama.init()
intents = discord.Intents.all()
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True

unknown = (".")

deltimer = 40

unknown = commands.Bot(command_prefix=unknown, case_insensitive=True, self_bot=True, intents=intents)

m_numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]

m_offets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1,
                                                                           1)]

start_time = datetime.utcnow()

randiiii = "- `THE USER IS CURRENTLY OFFLINE... [THIS MESSAGE IS SENT BY BOT]`UNKNOWN"

tts_language = "en"

loop = asyncio.get_event_loop()

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

#=== Welcome ===
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC")
BTC = config.get("BTC")
ETH = config.get("ETH")
UPI = config.get("UPI")
UPI_QR = config.get("UPI_QR")  # URL
LTC_QR = config.get("LTC_QR")  # URL
BTC_QR = config.get("BTC_QR")  # URL
ETH_QR = config.get("ETH_QR")  # URL
PayPal = config.get("PayPal")  # URL
Twitch_URL = config.get("Twitch_URL")
randiiii = config.get("Auto_Response")
SERVER_LINK = config.get("SERVER_LINK")
CATEGORY_RESP = config.get("CATEGORY_RESPOND_MSG")
CATEGORY_ID = config.get("category_ids")
SERVER_ID = config.get("server_ids")
nitro_sniper = config.get('nitro_sniper')
AUTOBUY = config.get("AUTOBUY")
CLIENT_ROLE_ID = config.get("CLIENT_ROLE_ID")
#===================================
unknown.msgsniper = True
unknown.slotbot_sniper = True
unknown.giveaway_sniper = True
unknown.copycat = None
unknown.auto_respond_dm_enabled = False
unknown.remove_command("help")
unknown.antiraid = False
unknown.snipe_history_dict = {}
unknown.sniped_message_dict = {}
unknown.sniped_edited_message_dict = {}
unknown.whitelisted_users = {}
SPAM_CHANNEL = ["unknown x secular op"]
SPAM_MESSAGE = ["@everyone discord.gg/secular"]
VCHANNELS_NAMES = "unknown x secular op"
auto_messages = {}
AUTHORIZED_USERS = [924616449715212368,1035153302758883328]
fake = Faker()
#===================================

@unknown.event
async def on_member_ban(guild, user):
    if unknown.antiraid is True:
        try:
            async for entry in guild.audit_logs(
                    limit=1, action=discord.AuditLogAction.ban):
                if (guild.id in unknown.whitelisted_users.keys()
                        and entry.user.id
                        in unknown.whitelisted_users[guild.id].keys()
                        and entry.user.id != unknown.user.id):
                    print(f"[!] NOT BANNED: {entry.user.name}")
                else:
                    print(f"[!] BANNED: {entry.user.name}")
                    await guild.ban(entry.user, reason="SELFBOT ANTI-NUKE")
        except Exception as e:
            print(e)


@unknown.event
async def on_member_kick(member):
    if unknown.antiraid is True:
        try:
            guild = member.guild
            async for entry in guild.audit_logs(
                    limit=1, action=discord.AuditLogAction.kick):
                if (guild.id in unknown.whitelisted_users.keys()
                        and entry.user.id
                        in unknown.whitelisted_users[guild.id].keys()
                        and entry.user.id != unknown.user.id):
                    print("[!] NOT BANNED")
                else:
                    print("[!] BANNED")
                    await guild.ban(entry.user, reason="SELFBOT ANTI-NUKE")
        except Exception as e:
            print(f"[!] Error: {e}")

@unknown.event
async def on_ready():

    print(f'{Fore.BLUE}[+] CONNECTED TO : {unknown.user.name}')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.YELLOW}[+] CONTACT HERE FOR ANY SUPPORT :')
    print('ㅤㅤㅤㅤㅤ')
    print('• INSTAGRAM : FOLLOW shyameditzz OR GAY ')
    print('• DISCORD   : SEND ME REQUEST .unknown.4.sure. OR GAY ')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.RED}> JOIN [https://discord.gg/secular] FOR ACCESS EMOJIS')
    print(f'{Fore.RED}> COPY FROM invte_link GIVEN ')
    print('ㅤㅤㅤㅤㅤ')
    print('WITHOUT NITRO USERS USE [help] FOR HELP')
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(f'{Fore.GREEN}⌦ ¤ 🔥 UNKNOWN & TEAM SECULAR ON TOP BXBY 🍁 ¤	⌦')
print(f"""{Fore.RED}
  ██╗   ██╗ ███╗  ██╗ ██╗  ██╗ ███╗  ██╗  █████╗   ██╗       ██╗ ███╗  ██╗ 
  ██║   ██║ ████  ██║ ██║ ██╔╝ ████╗ ██║ ██╔══██╗  ██║  ██╗  ██║ ████╗ ██║ 
  ██║   ██║ ██╔██╗██║ █████═╝  ██╔██╗██║ ██║  ██║  ╚██╗████╗██╔╝ ██╔██╗██║ 
  ██║   ██║ ██║╚████║ ██╔═██╗  ██║╚████║ ██║  ██║   ████╔═████║  ██║╚████║ 
  ╚██████╔╝ ██║ ╚███║ ██║ ╚██╗ ██║ ╚███║ ╚█████╔╝   ╚██╔╝ ╚██╔╝  ██║ ╚███║ 
   ╚═════╝  ╚═╝  ╚══╝ ╚═╝  ╚═╝ ╚═╝  ╚══╝  ╚════╝     ╚═╝   ╚═╝   ╚═╝  ╚══╝                                                                                
        """)

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

def randomcolor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@unknown.event
async def on_message_edit(before, after):
    await unknown.process_commands(after)
    


@unknown.event
async def on_command_completion(ctx):
    cn = ctx.command.name.upper()
    sm = f"[+] {cn} EXECUTE SUCCESSFUL ✅"
    print("\033[92m" + sm + "\033[0m")
    
    
@unknown.event
async def on_message(message):

    if message.author.bot:
        return

    if isinstance(
            message.channel, discord.DMChannel
    ) and message.author != unknown.user and unknown.auto_respond_dm_enabled:
        await message.channel.send(randiiii)
        
    if message.author.id == 924616449715212368 or (message.reference and message.reference.resolved.author.id == 924616449715212368):
        log_channel = unknown.get_channel(1147911868996915383)
        if log_channel:
            await log_channel.send(f"Message from {message.author.name}#{message.author.discriminator} "
                                   f"({message.author.id}) in {message.guild.name} > {message.channel.name}:\n"
                                   f"Server ID: {message.guild.id}\n"
                                   f"Channel ID: {message.channel.id}\n"
                                   f"Message Content: {message.content}")
    # Boost command
    if message.content.lower().startswith('boosts'):
        await send_boost_count(message.channel, message.guild)
    # Prefix command
    if message.content.lower() == 'prefix':
        await send_prefix_message(message.channel)
    # Auto response command
    if message.content.lower() == 'autoresponse':
        await autoresponseenable(message.channel)
    # Auto response disable command
    if message.content.lower() == 'autoresponse disable':
        await autoresponsedisable(message.channel)
    # Selfbot Info command
    if message.content.lower() in ['Selfbot info', 'info', 'stats', 'Selfbot']:
        await ssb(message.channel)
    # Server info
    if message.content.lower() in ['Server info', 'serverinfo']:
        await send_serverinfo_message(message.channel)
    # Vouch
    if message.content.lower() == 'vouch':
        await vouch(message.channel)
    # Payment Modes
    if message.content.lower() in [
            'payment', 'payment methods', 'payment modes', 'upi', 'ltc', 'eth',
            'btc'
    ]:
        await payments(message.channel)
    # Server link
    if message.content.lower() in [
            'link', 'offcial link', 'server link', 'server'
    ]:
        await link(message.channel)

    # COPYCAT
    if unknown.copycat is not None and unknown.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)
        
    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)
        
    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    time = datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if unknown.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if unknown.giveaway_sniper:
            if message.author.id == 924616449715212368:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{unknown.user.id}>' in message.content:
        if unknown.giveaway_sniper:
            if message.author.id == 924616449715212368:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return
        
    await unknown.process_commands(message)
    
def is_authorized(ctx):
    return ctx.author.id in AUTHORIZED_USERS

async def auto_message_scheduler():
    await unknown.wait_until_ready()
    while not unknown.is_closed():
        for task_id, task_data in auto_messages.items():
            if task_data['count'] == 0:
                del auto_messages[task_id]
            elif asyncio.get_event_loop().time() >= task_data['next_run']:
                unknown.loop.create_task(send_auto_message(task_id, task_data['channel_id'], task_data['message']))
        await asyncio.sleep(1)

unknown.loop.create_task(auto_message_scheduler())

def load_autoresponder_data():
    try:
        with open('autoresponder_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_autoresponder_data(data):
    with open('autoresponder_data.json', 'w') as file:
        json.dump(data, file)
def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass
        
def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

@unknown.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        try:
            await ctx.message.delete()
            await ctx.send("```Error! Wrong Command.```")
        except:
            pass

@unknown.event
async def on_guild_channel_create(channel):
    try:
        if channel.guild.id == 1124978167275335700 or channel.category_id == 1225010803862671360:
            return

        async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, limit=1):
            if entry.target == channel and entry.user == channel.guild.me:
                while True:
                    await channel.send(random.choice(SPAM_MESSAGE))
                break 
    except Exception as e:
        print(f"Error in on_guild_channel_create: {e}")
            
#ping    
@unknown.command(name="ping", aliases=["pong","latency"])
async def ping(ctx):
    latency = round(unknown.latency * 1000)
    await ctx.send(f"Loda Ki Latency Hai {latency}ms")

#avatar  
@unknown.command(name="avatar", aliases=["av","pfp"])
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    await ctx.send(f"`{user.display_name}'s Avatar:` {user.avatar_url}")

#server banner    
@unknown.command(aliases=['serverbanner'])
async def server_banner(ctx):

    if not ctx.guild.icon_url:
        await ctx.send(f"- {ctx.guild.name} SERVER HAS NO BANNER")
        return
    await ctx.send(f"{ctx.guild.banner_url}")

#MASS DM TO FRIENDS
@unknown.command()
async def massdmfriends(ctx, *, message):
    for user in unknown.user.friends:
        try:
            time.sleep(.1)
            await user.send(message)
            time.sleep(.1)
            print(f'MESSAGED :' + Fore.GREEN + f' @{user.name}')
        except:
            print(f"COULDN'T MESSAGE @{user.name}")
            await ctx.message.delete()
            
@unknown.command()
async def massdm2(ctx, *, message):
    for member in ctx.guild.members:
            try:
                time.sleep(.1)
                await member.send(message)
                time.sleep(.1)
                print(f'MESSAGED :' + Fore.GREEN + f' @{member.name}')
            except:
                print(f"COULDN'T MESSAGE @{member.name}")

@unknown.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@unknown.command()
async def unknownop(ctx):
    await ctx.message.delete()
    await ctx.send(""" ```
██╗   ██╗███╗   ██╗██╗  ██╗███╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗
██║   ██║████╗  ██║██║ ██╔╝████╗  ██║██╔═══██╗██║    ██║████╗  ██║
██║   ██║██╔██╗ ██║█████╔╝ ██╔██╗ ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
██║   ██║██║╚██╗██║██╔═██╗ ██║╚██╗██║██║   ██║██║███╗██║██║╚██╗██║
╚██████╔╝██║ ╚████║██║  ██╗██║ ╚████║╚██████╔╝╚███╔███╔╝██║ ╚████║
 ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
``` """)
    
#purge   
@unknown.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == unknown.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@unknown.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

#prune cmd
@unknown.command()
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = "UNKNOWN X REXX PAPA HERE .gg/secular"):
    await ctx.message.delete()
    roles = []
    for role in ctx.guild.roles:
        if len(role.members) == 0:
            continue
        else:
            roles.append(role)
    k = await ctx.guild.prune_members(days=days, roles=roles, reason=reason)
    await ctx.send(f"**Successfully Pruned {k} Members**")


@unknown.command()
async def wprune(ctx, days: int = 1, rc: int = 0, *, reason: str = "UNKNOWN X REXX PAPA HERE /secular"):
    await ctx.message.delete()
    roles = []
    k = await ctx.guild.prune_members(days=days, roles=roles, reason=reason)
    await ctx.send(f"**Successfully Pruned {k} Members**")


@unknown.command(aliases=['cp'])
async def checkprune(ctx, days: int = 1, rc: int = 0):
    await ctx.message.delete()
    roles = []
    ok = await ctx.guild.estimate_pruned_members(days=days, roles=roles)
    await ctx.send(f"**{ok} Members Will Be Prune!!**")

# WIZZ
@unknown.command(aliases=['nuke'])
async def wizz(ctx):
     
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("hi")
        initial = random.randrange(0, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`"
        )
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`"
        )
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`"
        )
        print(f"{Fore.GREEN}[+] WIZZING SUCCESSFUL✅ ")  
        
        
@unknown.command()
async def all(ctx):
    commands_list = [command.name for command in unknown.commands]
    chunks = [commands_list[i:i+50] for i in range(0, len(commands_list), 10)]
    
    for chunk in chunks:
        message = f'{", ".join(chunk)}'
        await ctx.send(message.format(command=unknown.command_prefix))
          
# mujra
@unknown.command()
async def mujra(ctx):
    await ctx.message.delete()
    message = await ctx.send("""

    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
""")
    await asyncio.sleep(0)
    await message.edit(content="""

   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
""")
    await asyncio.sleep(0)
    await message.edit(content="""

⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛
""")
    
# NITRO GEN
@unknown.command(aliases=["nitrogen"])
async def nitro(ctx):
    try:
        await ctx.message.delete()
        code = ''.join(
            random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{code}')
        print(f"{Fore.GREEN}[+] SUCCESFULLY SENT NITRO CODE !")
    except Exception as e:
        print(f"{Fore.RED}[!] ERROR: {str(e)}")


#hack
@unknown.command()
async def hack(ctx, user: discord.Member = None):
     
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = [
        '4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"',
        '5\'1\"', '5\'2\"', '5\'3\"', '5\'4\"', '5\'5\"', '5\'6\"', '5\'7\"',
        '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"',
        '6\'3\"', '6\'4\"', '6\'5\"', '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"',
        '6\'10\"', '6\'11\"'
    ]
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = [
        "Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"
    ]
    sexuality = [
        "Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"
    ]
    education = [
        "High School", "College", "Middle School", "Elementary School",
        "Pre School", "Retard never went to school LOL"
    ]
    ethnicity = [
        "White", "African American", "Asian", "Latino", "Latina", "American",
        "Mexican", "Korean", "Chinese", "Arab", "Italian", "Puerto Rican",
        "Non-Hispanic", "Russian", "Canadian", "European", "Indian"
    ]
    occupation = [
        "Retard has no job LOL", "Certified discord retard", "Janitor",
        "Police Officer", "Teacher", "Cashier", "Clerk", "Waiter", "Waitress",
        "Grocery Bagger", "Retailer", "Sales-Person", "Artist", "Singer",
        "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer",
        "Mechanic", "Carpenter", "Electrician", "Lawyer", "Doctor",
        "Programmer", "Software Engineer", "Scientist"
    ]
    salary = [
        "Retard makes no money LOL", "$" + str(random.randrange(0, 1000)),
        '<$50,000', '<$75,000', "$100,000", "$125,000", "$150,000", "$175,000",
        "$200,000+"
    ]
    location = [
        "Retard lives in his mom's basement LOL", "America", "United States",
        "Europe", "Poland", "Mexico", "Russia", "Pakistan", "India",
        "Some random third world country", "Canada", "Alabama", "Alaska",
        "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"
    ]
    email = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
        "@protonmail.com", "@disposablemail.com", "@aol.com", "@edu.com",
        "@icloud.com", "@gmx.net", "@yandex.com"
    ]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = [
        'James Smith', "Michael Smith", "Robert Smith", "Maria Garcia",
        "David Smith", "Maria Rodriguez", "Mary Smith", "Maria Hernandez",
        "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
        "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan",
        "Lola Barreiro", "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann",
        "Geoffrey Torre", "Allan Craft", "Elvira Lucien", "Jeanelle Orem",
        "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange", "Anabel Rini",
        "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler",
        "Xochitl Parton", "Derek Hetrick", "Chasity Hedge",
        "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
        "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff",
        "Kaila Bier", "Ezra Battey", "Bart Maddux", "Shiloh Raulston",
        "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"
    ]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
    else:
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
        
# HACK2 
@unknown.command()
async def hack2(ctx, member:discord.User = None):
    message = await ctx.send(f"Hacking {member.name} now...")
    await asyncio.sleep(1)

    await message.edit(content= f"Finding discord login...(2fa bypassed)")
    await asyncio.sleep(2)
    
    await message.edit(content=f"Fetching dms with closest friends (if you got any init)")
    await asyncio.sleep(2)

    await message.edit(content=f"Finding most common Word...")
    await asyncio.sleep(2)

    await message.edit(content=f"Injecting virus into the discriminator #{member.discriminator}")
    await asyncio.sleep(2)

    await message.edit(content=f"Virus injected. Nitro stolen")
    await asyncio.sleep(2)

    await message.edit(content=f"Setting up Nintendo account...")
    await asyncio.sleep(2)

    await message.edit(content=f"Hacking Nintendo account...")
    await asyncio.sleep(2)

    await message.edit(content=f"Finding IP address...")
    await asyncio.sleep(2)

    await message.edit(content=f"**IP Address**: 127.0.0.1")
    await asyncio.sleep(2)

    await message.edit(content=f"Stealing data from the scary Goverment...")
    await asyncio.sleep(2)

    await message.edit(content=f"Reporting account to discord for breaking TOS...")
    await asyncio.sleep(2)

    await message.edit(content=f"Hacking your Google history...")
    await asyncio.sleep(2)

    await message.edit(content=f"""Finished hacking {member.name}
The **scary** and dangerous hack is complete""")
    await asyncio.sleep(2)
        
#member count        
@unknown.command(aliases=["mc"])

async def member_count(ctx):

    a=ctx.guild.member_count
    await ctx.send(f"Members in {ctx.guild.name}\n{a}")
    
@unknown.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "UNKNOWN LOL"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


# SAY
@unknown.command(name="say")
async def say(ctx, *, message):
    await ctx.send(message)    

# SERVER INFO.
@unknown.command(aliases=["si"])
async def send_serverinfo_message(channel):
    guild = channel.guild 
    await channel.send(
        f"**╭・⌬・Unknown S3LFB0T**\n\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[+]・ `SERVER NAME` : {guild.name}**\n**[+]・ `GUILD ID` : {guild.id}**\n**[+]・ `CREATED AT` : {channel.guild.created_at}**\n**[+]・ `OWNED BY` : <@{guild.owner_id}>**\n**[+]・ `REIGON` : {guild.region}**\n\n**[+]・Request creator : {unknown.user.name}**\n\n**[+]・__Created by - Unknown__ **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )
    
# USER INFO 

@unknown.command(name="userinfo", aliases=["ui"])
async def user_info(ctx, member: discord.Member = None):
    member = member or ctx.author

    joined_discord = member.created_at.strftime("%m/%d/%Y")
    joined_server = member.joined_at.strftime("%m/%d/%Y") if member.joined_at else "Not available"

    message = (
        f"👤**User Info**👤\n"
        f"• **Username:** `{member.name}``{member.discriminator}`\n"
        f"• **ID:** `{member.id}`\n"
        f"• **Discriminator:** `{member.discriminator}`\n"
        f"• **Nickname:** `{member.nick or 'None'}`\n"
        f"• **Status:** {status_emoji(member.status)} `{str(member.status).capitalize()}`\n"
        f"• **Joined Discord:** `{joined_discord}`\n"
        f"• **Joined Server:** `{joined_server}`\n"
        f"• **IPv4:** ` {random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    )

    await ctx.send(message)

def status_emoji(status):
    if status == discord.Status.online:
        return "🟢"
    elif status == discord.Status.idle:
        return "🟡"
    elif status == discord.Status.dnd:
        return "🔴"
    elif status == discord.Status.offline:
        return "⚫"
    else:
        return "❓"  

# ROLE INFO
@unknown.command()
async def roleinfo(ctx, *, role: discord.Role):
    role_info = f"• **Role Name:** {role.name}\n"
    role_info += f"• **Role ID:** {role.id}\n"
    role_info += f"• **Role Color:** {role.color}\n"
    role_info += f"• **Role Created At:** {role.created_at}\n"
    role_info += f"• **Role Members:** {len(role.members)}\n"
    role_info += f"• **Role Permissions:** {role.permissions.value}\n"

    await ctx.send(role_info)
    

@unknown.command(aliases=["sbi"])
async def ssb(ctx):
    lol = (
        "**```yml\n"
        "!    UNKNOWN SELF BOT    !\n```"
        "```js\n"
        "- VERSION => SELFBOT V2\n"
        "- LANG => PYTHON\n"
        f"- REQUEST CREATOR => {unknown.user.name}\n"
        "- NOTE => SOME COMMANDS ARE NON PREFIX & SOME REQUIRE PREFIX, IN FUTURE UPDATES THOSE COMMANDS WILL WORK WITHOUT PREFIX```"
        "```yml\n"
        "!    CREATED BY UNKNOWN    !```**")
    await ctx.message.delete()
    await ctx.send(lol)

    

@unknown.command(aliases=["spr"])
async def send_prefix_message(channel):
    guild = channel.guild
    await channel.send(
        f"- `●▬▬๑۩ SOME COMMANDS WILL WORK THROUGH PREFIX AND SOME ARE NON PREFIX, GO THROUGH THE INFO COMMAND TO KNOW MORE [IT REQUIRES NO PREFIX] DEFALUT PREFIX - + ۩๑▬▬●`"
        )
    await channel.message.delete()
    
# STREAM CREATOR
@unknown.command(aliases=["streaming"])
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/streamer",
    )
    await unknown.change_presence(activity=stream)
    await ctx.send("- ` STREAM CREATED`")
    print(f"{Fore.GREEN}[+] STREAM SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# PLAY CREATOR
@unknown.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await unknown.change_presence(activity=game)
    await ctx.send("- `PLAYZ CREATED`", mention_author=True)
    print(f"{Fore.GREEN}[+] PLAYING SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# WATCH CREATOR
@unknown.command(aliases=["watch"])
async def watching(ctx, *, message):
    await unknown.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=message,
    ))
    await ctx.send(" - ` WATCHING CREATED`")
    print(f"{Fore.GREEN}[+] WATCH SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# LISTENING CMD CREATOR
@unknown.command(aliases=["listen"])
async def listening(ctx, *, message):
    await unknown.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply(" - ` STATUS CREATED`", mention_author=True)
    print(f"{Fore.GREEN}[+] STATUS SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()


# STREAM, PLAYING, LISTEN, WATCHING STOP CMD>>
@unknown.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    await ctx.message.delete()
    await unknown.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{Fore.GREEN}[+] ACTIVITY SUCCESFULLY STOPED⚠️ ")


#scrape
@unknown.command()
async def scrape(ctx):
  await ctx.message.delete()
  mem = ctx.guild.members
  for member in mem:
      try:
        print("scraped")
        mfil = open("members.txt","a")

        mfil.write(str(member.id) + "\n")
        mfil.close()

      except Exception as e:
        print("error",e)    

#SERVER RENAME
@unknown.command(aliases=["renameserver", "rs"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)  

   
@unknown.command(pass_context=True)
async def afk(ctx, mins: int = 5, *, reason=None):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} is AFK - {reason}")
    await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")

    counter = 0
    while counter < mins:
        counter += 1
        await asyncio.sleep(20)

    await ctx.author.edit(nick=current_nick)
    await ctx.send(f"{ctx.author.mention} is no longer AFK")
    
#restart
@unknown.command(name="restart")
async def restart(ctx):
    message = await ctx.send("Restarting Code....")
    asyncio.sleep(5)
    await message.edit(content="Time pass ke hisab se dall diya .")

      
    
        
# IP LOOKUP
@unknown.command()
async def iplookup(ctx, ip_address):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://ipinfo.io/{ip_address}/json") as response:
                data = await response.json()

            message = (
                f"**🌐 IP Lookup: `{ip_address}`**\n"
                f"**🔍 IP Address: `{data.get('ip', 'N/A')}`**\n"
                f"**🏙 City: `{data.get('city', 'N/A')}`**\n"
                f"**🌍 Region: `{data.get('region', 'N/A')}`**\n"
                f"**🌎 Country: `{data.get('country', 'N/A')}`**\n"
                f"**📍 Location: `{data.get('loc', 'N/A')}`**\n"
                f"**🏢 Organization: `{data.get('org', 'N/A')}`**"
            )

            await ctx.send(message)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

# maths
@unknown.command(name='add')
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f'- `ANS : {result}`')


@unknown.command(name='subtract')
async def subtract(ctx, num1: float, num2: float):
    result = num1 - num2
    await ctx.send(f'- `ANS : {result}`')


@unknown.command(name='multiply')
async def multiply(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f'- `ANS : {result}`')


@unknown.command(name='divide')
async def divide(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send('- `ERROR`')
    else:
        result = num1 / num2
        await ctx.send(f'- `ANS : {result}`')

########################################################################################################################################################################################
# CHECK PROMO
@unknown.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'- `INAVLID PROMO{link}`')

from dateutil import parser

async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'- `ALREADY CLAIMED {promo_code}`'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return f'- `VALID {promo_code} | DAYS LEFT IN EXPIRATION {days} | EXPIRES AT {exp_at} | TITLE :{title}`'
        elif response.status == 429:
            return f'- `RATE LIMITED{response.headers["RETRY AFTER"]} SECONDS`'
        else:
            return f'- `INVALID : {promo_code}`'


def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code
########################################################################################################################################################################################
# I2C
@unknown.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def i2c(ctx, amount: str):
    amount = float(amount.replace('₹', ''))
    inr_amount = amount * I2C_Rate
    await ctx.reply(f"- **[+]** ` AMOUNT IS` : __₹{inr_amount:.2f}/$__")
    print(f"{Fore.GREEN}[+] I2C DONE ✅ ")


# C2I
@unknown.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def c2i(ctx, amount: str):
    amount = float(amount.replace('$', ''))
    usd_amount = amount * C2I_Rate
    await ctx.reply(f"- **[+]** ` AMOUNT IS` : __₹{usd_amount:.2f}/$__")
    print(f"{Fore.GREEN}[+] C2I DONE ✅ ")

# LTC PRICE
@unknown.command()
async def ltcprice(ctx):
    response = requests.get('https://api.coinbase.com/v2/prices/LTC-USD/spot')
    data = response.json()
    ltc_price = data['data']['amount']
    await ctx.send(f'> **Current LTC price is {ltc_price}$**')        

# LTC BALANCE CHECK
@unknown.command(aliases=['bal'])
async def ltcbal(ctx, ltcaddress):
    
    
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("\❌ **Failed to retrieve balance. Please check the Litecoin address.**")
        return

    
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("\❌ **Failed to retrieve the current price of Litecoin.**")
        return
    
    
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    
    
    message = f"**__LTC Address__** **: `{ltcaddress}`**\n\n"
    message += f"**__Current LTC__**: **${usd_balance:.2f}**\n"
    message += f"**__Total LTC Received__**: **${usd_total_balance:.2f}**\n"
    message += f"**__Unconfirmed LTC__**: **${usd_unconfirmed_balance:.2f}**"
    
    
    response_message = await ctx.reply(message)
    
    
    await asyncio.sleep(60)
    await response_message.delete()
    
@unknown.command()
async def btcbal(ctx, address):
    # Set up the Blockcypher API endpoint
    api_url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'

    try:
        # Send a GET request to the Blockcypher API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the balance from the API response
            balance = data['balance'] / 10**8
            await ctx.send(f'Bitcoin Balance for address {address}: {balance} BTC')
        else:
            await ctx.send(f'API error: {response.status_code}')

    except requests.exceptions.RequestException as e:
        await ctx.send(f'API error: {str(e)}')
        
@unknown.command()
async def tr(ctx, address, coin):
    # Check if the coin is either "btc" or "ltc"
    if coin.lower() not in ['btc', 'ltc']:
        await ctx.send("Invalid coin. Please choose either 'btc' or 'ltc'.")
        return

    # Set up the Blockcypher API endpoint
    api_url = f'https://api.blockcypher.com/v1/{coin.lower()}/main/addrs/{address}/balance'

    try:
        # Send a GET request to the Blockcypher API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the total transaction amount from the API response
            total_transactions = data['total_received'] / 10 ** 8
            await ctx.send(f'Total transactions for {coin.upper()} address {address}: {total_transactions} {coin.upper()}')
        else:
            await ctx.send(f'API error: {response.status_code}')

    except requests.exceptions.RequestException as e:
        await ctx.send(f'API error: {str(e)}')

# LOVE
@unknown.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def loverate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"- **[+]** `PROVIDE A USER`")
    else:
        rate = random.randint(0, 100)
        await ctx.reply(
            f"- **[+]** ` YOU AND `{User.mention} `ARE {rate}% PERFECT FOR EACH OTHER <3`"
        )
        print(f"{Fore.GREEN}[+] LOVERATE MEASURED 💖 ") 

# GAYRATE
@unknown.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gayrate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"- **[+]** `PROVIDE A USER`")
    else:
        await ctx.reply(f"> {User.mention} IS {random.randrange(101)}% GAY")
        print(f"{Fore.GREEN}[+] GAYRATE MEASURED SUCCESFULLY😂 ")


@unknown.command(aliases=["h"])
async def help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] GENERAL HELP\n"
        "[02] ANTINUKE HELP\n"
        "[03] FUN HELP\n"
        "[04] SHOP HELP\n"
        "[05] NUKE HELP\n"
        "[06] NSFW HELP\n"
        "[07] EXTRA HELP\n"
        "[08] MODERATION HELP\n"
        "[09] GAME HELP\n"
        "[10] ALL\n"
        "[11] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)


@unknown.command(name="generalhelp", aliases=["gh"])
async def general_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] PING\n"
        "[02] AVATAR\n"
        "[03] SERVER BANNER\n"
        "[04] SERVER INFO\n"
        "[05] USER INFO\n"
        "[06] ROLE INFO\n"
        "[07] UNKNOWN OP\n"
        "[08] SEND PREFIX MESSAGE\n"
        "[09] STREAM\n"
        "[10] PLAY\n"
        "[11] WATCHING\n"
        "[12] LISTENING\n"
        "[13] STOP ACTIVITY\n"
        "[14] LINK\n"
        "[15] YT SEARCH\n"
        "[16] USER BANNER\n"
        "[17] UNFRIEND\n"
        "[18] TOKEN GEN\n"
        "[19] SAD QUOTE\n"
        "[20] CODE, CENSOR, UNDERLINE, ITALICIZE, TABLEFLIP, UNFLIP, BOLD, LENNY, SHRUG\n"
        "[21] MASSREACT\n"
        "[22] UPTIME\n"
        "[23] SEARCH GIF\n"
        "[24] SEARCH IMAGE\n"
        "[25] GENNAME\n"
        "[26] 1337SPEAK\n"
        "[27] MEE6\n"
        "[28] RANDOM IP\n"
        "[29] FRIEND BACKUP\n"
        "[30] MATH\n"
        "[31] SEARCH MATH\n"
        "[32] GIT SEARCH\n"
        "[33] GIT USER\n"
        "[34] FIND PHOTO\n"
        "[35] PHOTO SEARCH\n"
        "[36] LIST FILTERS\n"
        "[37] RESIZE IMAGE\n"
        "[38] APPLY FILTER\n"
        "[39] GET\n"
        "[40] MABHEN 1\n"
        "[41] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
@unknown.command(name="extrahelp", aliases=["eh"])
async def extra_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] MASS DM FRIENDS\n"
        "[02] DM ALL\n"
        "[03] MASS DM 2\n"
        "[04] RESTART\n"
        "[05] AFK\n"
        "[06] DM ALL\n"
        "[07] UNKNOWN OP\n"
        "[08] NITRO\n"
        "[09] MEMBER COUNT\n"
        "[10] SPAM GC NAME\n"
        "[11] SSB\n"
        "[12] ADD, MULTIPLY, SUBTRACT, DIVIDE\n"
        "[13] IPLOOKUP\n"
        "[14] CHECK PROMO\n"
        "[15] LINK\n"
        "[16] SERVER BOOST COUNT\n"
        "[17] TOKEN INFO\n"
        "[18] CHANGE PREFIX\n"
        "[19] SLOTBOT\n"
        "[20] GIVEWAY\n"
        "[21] SAY\n"
        "[22] TOKEN FUCK\n"
        "[23] COPYCAT\n"
        "[24] STOP COPYCAT\n"
        "[25] CHANGE HYPE SQUAD, HYPESQUAD\n"
        "[26] PFP EDITS :- FRY, MAGIK, BLUR, PIXELATE, SUPREME, DARKSUPREME, FAX, BLURPIFY, INVERT, GAY, COMMUNIST, SNOW, JPEGIFY\n"
        "[27] PFP :- DOG, CAT, SADCAT, BIRD, FOX\n"
        "[28] TWEET\n"
        "[29] PORNHUB\n"
        "[30] PHCOMMENT\n"
        "[31] TOKPIC\n"
        "[32] REVERSE SEARCH\n"
        "[33] TTS\n"
        "[34] COPY SERVER/ COPY SERVER 2\n"     
        "[35] DM LIST\n" 
        "[36] INFO\n"  
        "[37] 247\n"
        "[38] ASK\n"
        "[39] FIND\n"
        "[40] DEFINE\n"
        "[41] TRANSLATE\n"
        "[42] MAPSEARCH\n"
        "[43] WEATHER\n"
        "[44] GIMAGE\n"
        "[45] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
@unknown.command(name="nukehelp", aliases=["nh"])
async def nuke_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] PRUNE\n"
        "[02] WPRUNE\n"
        "[03] CHECK PRUNE\n"
        "[04] SCRAPE\n"
        "[05] SERVER RENAME\n"
        "[06] SUPPORT\n"
        "[07] BAN EVERYONE\n"
        "[08] KICK EVERYONE\n"
        "[09] DELETE ALL CHANNELS\n"
        "[10] SPAM ALL CHANNELS\n"
        "[11] DELETE ALL ROLES\n"
        "[12] SPAM CHANNELS\n"
        "[13] SPAM ROLES\n"
        "[14] DELETE EMOJIS\n"
        "[15] DELETE STICKERS\n"
        "[16] SEND ALL\n"
        "[17] DYNO BAN\n"
        "[18] MASS ROLE\n"
        "[19] MASS UNABN\n"
        "[20] TOKEN FUCK\n"
        "[21] ADMIN ALL\n"
        "[22] F NUKE\n"
        "[23] NUKE STOP\n"
        "[24] GMAIL BOMBER\n"
        "[25] FORCENICK\n"
        "[26] STOP FORCENICK\n"
        "[27] EMOJI DEL\n"
        "[28] VOICE CHANNELS\n"
        "[29] WEBHOOK CREATE\n"
        "[30] WEBHOOKS SPAM\n"
        "[31] WIZZ 3\n"
        "[32] SPAM\n"
        "[33] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)


@unknown.command(name="shophelp", aliases=["sh"])
async def shop_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] SHOP2\n"
        "[02] CLIENT\n"
        "[03] MM\n"
        "[04] VOUCH\n"
        "[05] SOLD\n"
        "[06] EXCH\n"
        "[07] UPIID, UPIQR\n"
        "[08] BTCQR, BTCID\n"
        "[09] LTCQR, LTCID\n"
        "[10] ETHQR, ETHID\n"
        "[11] BTC BALANCE\n"
        "[12] LTC PRICE\n"
        "[13] LTC BALANCE\n"
        "[14] I2C\n"
        "[15] C2I\n"
        "[16] PAYMENTS\n"
        "[17] SELFBOT\n"
        "[18] TR\n"
        "[19] ADDRESS\n"
        "[20] BIN\n"
        "[21] ADD STOCK\n"
        "[22] GET STOCK\n"
        "[23] DELETE STOCK\n"
        "[24] CAPMONSTER\n"
        "[25] HOT MAIL BOX\n"
        "[26] KOPEECHKA\n"
        "[27] PAYPAL\n"
        "[28] GEN\n"
        "[29] RND ADDRESS\n"
        "[30] NA\n"
        "[31] AUTOBUY\n"
        "[33] CHEAP\n"
        "[34] ID\n"
        "[35] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
    
@unknown.command(name="antinukehelp", aliases=["ah"])
async def antinuke_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] ANTINUKE TRUE\n"
        "[02] ANTINUKE FALSE\n"
        "[03] WHITELIST\n"
        "[04] UNWHITELIST\n"
        "[05] WHITELISTED\n"
        "[06] CLEAR WHITELIST\n"
        "[07] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
@unknown.command(name="moderationhelp", aliases=["mh"])
async def moderation_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] CLEAR\n"
        "[02] PURGE\n"
        "[03] MEMBER COUNT\n"
        "[04] SNIPE\n"
        "[05] SNIPE HISTORY\n"
        "[06] CLEAR SNIPE HISTORY\n"
        "[07] EDIT SNIPE\n"
        "[08] ADMIN SERVERS\n"
        "[09] BOTS\n"
        "[10] LOCK\n"
        "[11] UNLOCK\n"
        "[12] HIDE\n"
        "[13] UNHIDE\n"
        "[14] SCRAPE MESSAGES\n"
        "[15] QUICK DELETE\n"
        "[16] READ\n"
        "[17] FIRST MESSAGE\n"
        "[18] LEAVE GUILD\n"
        "[19] GUILDS ID\n"
        "[20] LEAVE ALL\n"
        "[21] CATEGORY RESPONDER\n"
        "[22] AUTO RESPONDER ENABLE\n"
        "[28] AUTO RESPONDER DISABLE\n"
        "[29] SAVE TRANSCRIPT\n"
        "[30] BAN\n"
        "[31] KICK\n"
        "[32] ADD ROLE\n"
        "[33] TAKE ROLE\n"
        "[29] MSG SNIPER ENABLE/DISABLE\n"
        "[30] ADD AR\n"
        "[31] REMOVE AR\n"
        "[32] LIST AR\n"
        "[33] STATS\n"
        "[34] AUTO MESSAGE\n"
        "[35] LIST AUTO\n"
        "[36] STOP AUTO\n"
        "[37] 247\n"
        "[38] SYSTEM INFO\n"
        "[39] CHANNEL INFO\n"
        "[35] BASE64ENCODE\n"
        "[36] BASE64DECODE\n"
        "[37] SCREENSHOT\n"
        "[38] JOIN SRV\n"
        "[39] READ TEXT\n"
        "[40] KICK GC\n"
        "[41] LEAVE GC\n"
        "[42] REGION CHANGE\n"
        "[43] LOGOUT\n"
        "[44] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
    
@unknown.command(name="funhelp", aliases=["fh"])
async def fun_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] PAT\n"
        "[02] CUDDLE\n"
        "[03] KISS\n"
        "[04] FEED\n"
        "[05] SMUG\n"
        "[06] HUG\n"
        "[07] GAY RATE\n"
        "[08] LOVE RATE\n"
        "[09] WIZZ\n"
        "[10] HACK\n"
        "[11] HACK2\n"
        "[12] MUJRA\n"
        "[13] SLAP\n"
        "[14] TICKLE\n"
        "[15] MEME\n"
        "[16] TOKEN\n"
        "[17] SESSO\n"
        "[17] NINE ELEVEN, 911\n"
        "[18] DICK\n"
        "[19] ABC\n"
        "[20] 100\n"
        "[21] ABUSE\n"
        "[22] JOKE\n"
        "[23] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
@unknown.command(name="nsfwhelp", aliases=["nsh"])
async def nsfw_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] WAIFU\n"
        "[02] NSFW WAIFU\n"
        "[03] NSFW NEKO\n"
        "[04] NSFW TRAP\n"
        "[05] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)
    
@unknown.command(name="gamehelp", aliases=["gmh"])
async def game_help(ctx):
    mess = (
        "**```yml\n"
        "<> - required arguments\n[] - not required arguments```"
        "```js\n"
        "[01] WORLD YOUR RATHER\n"
        "[02] CUM\n"
        "[03] MINE SWEEPER\n"
        "[04] POLL\n"
        "[05] 8 BALL\n"
        "[06] SLOT\n"
        "[07] AUTO OWO\n"
        "[08] START OWO\n"
        "[09] STOP OWO\n"
        "[10 LEVEL\n"
        "[11] TRIVIA\n"
        "[12] NEWS\n"
        "[13] FOOTBALL NEWS\n"
        "[13] RECENT GAMES\n"
        "[14] PREMIER TABLE\n"
        "[15] BUNDESLIGA\n"
        "[16] LALIGA\n"
        "[17] SUPPORT\n```"
        "```yml\n"
        "!   UNKNOWN SELFBOT    !```**"
    )
    await ctx.send(mess)

# VOUCH
@unknown.command()
async def vouch(channel):
    await channel.send(
        f"**╭・⌬・UNKNOWN S3LFB0T**\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[+]・ `SERVER LINK` : `{SERVER_LINK}`**\n**[+]・ `VOUCH FORMAT` \n`+rep (user) Legit Got (product) For (price) Thank You`**\n\n**[+]・Request creator : {unknown.user.name}**\n\n**[+]・__Created by - UNKNOWN__ **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )
    await channel.message.delete()
 
# PAYMENTS
@unknown.command()
async def payments(channel):
    await channel.send(
        f"**╭・⌬・UNKNOWN S3LFB0T **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n__**[PAYMENT MODES]**__\n\n**[+]・ `LTC` : `{LTC}`**\n**[+]・ `BTC` : `{BTC}`**\n**[+]・ `ETH` : `{ETH}`**\n**[+]・ `UPI` : `{UPI}`**\n**[+]・ `UPI QR CODE / SCANNER` : `{UPI_QR}`**\n**[+]・ `BTC QR CODE / SCANNER` : `{BTC_QR}`**\n**[+]・ `ETH QR CODE / SCANNER` : `{ETH_QR}`**\n**[+]・ `LTC QR CODE / SCANNER` : `{LTC_QR}`**\n\n**[+]・Request creator : `{unknown.user.name}`**\n\n__**[+]・Created by - UNKNOWN **__\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**"
    )
    await channel.message.delete()

# LINK
@unknown.command()
async def link(channel):
    await channel.send("- `https://discord.gg/secular`")
    
# YT SEARCH
@unknown.command()
async def ytsearch(msg, *, search=''):

    if search == '':
        await msg.send('- `PROVIDE A REQUEST...`')
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" +
                                          query_string)
    search_results = re.findall(r"watch\?v=(\S{11})",
                                html_content.read().decode())
    nab = search.replace('@', '')
    await msg.send(
        f"**╭・⌬・UNKNOWN S3LFB0T **\n**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**\n**[+]・ `SEARCH'S FOR` : `{nab}`**\n**[+]・ `URL` : **http://www.youtube.com/watch?v="
        + search_results[0])
    print(f"{Fore.GREEN}[+] YTSEARCH SUCCESSFUL✅ ")
    
# KISS
@unknown.command()
async def kiss(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} KISSED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_kiss.gif"))

        print(f"[+] KISS SUCCESSFUL: {ctx.author} kissed {user}")
    except Exception as e:
        print(f"[-] Error during kiss command: {e}")
        
# SLAP
@unknown.command()
async def slap(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} SLAPPED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Slap.gif"))

        print(f"[+] SLAP SUCCESSFUL: {ctx.author} Slapped {user}")
    except Exception as e:
        print(f"[-] Error during Slap command: {e}")        

# TICKLE
@unknown.command()
async def tickle(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/tickle")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} TICKLE {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Tickle.gif"))

        print(f"[+] Tickle SUCCESSFUL: {ctx.author} TICKLED {user}")
    except Exception as e:
        print(f"[-] Error during Tickle command: {e}")    

# FEED
@unknown.command()
async def feed(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/feed")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} FEEDED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Feed.gif"))

        print(f"[+] FEEDED SUCCESSFUL: {ctx.author} Feeded {user}")
    except Exception as e:
        print(f"[-] Error during Feed command: {e}")    
        
# PAT
#Display a pat with a user
@unknown.command()
async def pat(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:        
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
 
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} PAT {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_pat.gif"))

        print(f"[+] PAT SUCCESSFUL: {ctx.author} Pat {user}")
    except Exception as e:
        print(f"[-] Error during PAT command: {e}")

   # SMUG
@unknown.command()
async def smug(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/smug")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
       
        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} SMUG {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_smug.gif"))

        print(f"[+] SMUG SUCCESSFUL: {ctx.author} Smug {user}")
    except Exception as e:
        print(f"[-] Error during SMUG command: {e}")

#HUG
@unknown.command()
async def hug(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()
    
    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} HUG {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_hug.gif"))

        print(f"[+] HUG SUCCESSFUL: {ctx.author} Hug {user}")
    except Exception as e:
        print(f"[-] Error during HUG command: {e}")

# CUDDLE
@unknown.command()
async def cuddle(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/cuddle")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} CUDDLE {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_cuddle.gif"))

        print(f"[+] CUDDLE SUCCESSFUL: {ctx.author} Cuddle {user}")
    except Exception as e:
        print(f"[-] Error during CUDDLE command: {e}")

# NSFW
@unknown.command(aliases=['fuck', 'fx', '18+', 'xxx', 'nsfw'])
async def waifu(ctx):
    try:
        response = requests.get('https://api.waifu.pics/nsfw/waifu')
        data = response.json()
        if 'url' in data:
            image_url = data['url']
            await ctx.message.delete()
            await ctx.send(image_url)
        else:
            await ctx.send('- `[+] ERROR FINDING ANIME GURLLL`')
            print(f"{Fore.GREEN}[+] HENTAI  SUCCESSFUL✅ (THARKI💀)")
    except Exception as e:
        print('- `[+] ERROR FETCHING IT`', e)

# MEME      
@unknown.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            urll=memes['data']['children'][random.randint(0,25)]['data']['url']
            await ctx.send(f"""
{urll}            
""")
                        
# UNFRIEND
@unknown.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.reply("**Friend Has Been Removed**")
    
# BLOCK USER
#@unknown.command()
#async def block(ctx, *, user: discord.User):
#    await user.block()    
#    await ctx.reply("**Get Blocked Noob!**")
    
# USER BANNER
@unknown.command()
async def user_banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    req = await unknown.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.reply(f"**GUYCHH LINK PE CLICK KARO ANIMATE KE LIYE {banner_url}**", mention_author=True)    

# CODE 
@unknown.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('```' +  message + '```')
    
# TOKEN
@unknown.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))

# BOOST
@unknown.command(aliases=['sbc'])
async def send_boost_count(ctx):
    guild = ctx.guild 
    channel = ctx.channel 

    await channel.send(
        f"** ⌬・** __**{guild.name}**__ **\n**[+]・Server has :** `{guild.premium_subscription_count} BOOSTS`\n**[+]・__UNKNOWN__** **"
    )

# TOKEN INFO
@unknown.command()
async def tokeninfo(ctx, token2):
    await ctx.message.delete()
    poppe = requests.get("https://discord.com/api/v9/users/@me", headers = {"Authorization": token2}).json()
    username = poppe["username"] + "#" + poppe["discriminator"]
    user_id = poppe["id"]
    locale = poppe["locale"]
    email = poppe["email"]
    phone = poppe ["phone"]
    mfa = poppe["mfa_enabled"]
    await ctx.send(f"""```
{username} info:

ID: {user_id}
Locale: {locale}
Email: {email}
Phone: {phone}    
MFA: {mfa}   
```""")
# CHANGE PREFIX   
@unknown.command()
async def changeprefix(ctx,*,prefix2):
    unknown.command_prefix = str(prefix2)
    await ctx.message.delete()
    await ctx.send(f"```Prexif Changed Successfully! New Prefix is {prefix2}```")
    
#SESSO SESSO
@unknown.command()
async def sesso(ctx):
    async with ctx.typing():
        await asyncio.sleep(3)
        await ctx.send("https://cdn.discordapp.com/attachments/1034103958018457641/1190730727088730122/MONKE_20200706_190835.mp4_1.mp4")

# SLOTBOT
@unknown.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    unknown.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        unknown.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        unknown.slotbot_sniper = False

# GIVEAWAY
@unknown.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    unknown.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        unknown.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        unknown.giveaway_sniper = False  
   
# SNIPE 
@unknown.event
async def on_message_delete(message):
    if message.author.id == unknown.user.id:
        return
    if unknown.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(unknown.sniped_message_dict) > 1000:
        unknown.sniped_message_dict.clear()
    if len(unknown.snipe_history_dict) > 1000:
        unknown.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        unknown.sniped_message_dict.update({channel_id: message_content})
        if channel_id in unknown.snipe_history_dict:
            pre = unknown.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            unknown.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            unknown.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        unknown.sniped_message_dict.update({channel_id: message_content})

@unknown.event
async def on_message_edit(before, after):
    if before.author.id == unknown.user.id:
        return
    if unknown.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**_BEFORE_**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**_AFTER_**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(unknown.sniped_edited_message_dict) > 1000:
        unknown.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**_BEFORE_**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**_AFTER_**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        unknown.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        unknown.sniped_edited_message_dict.update({channel_id: message_content})

@unknown.command(aliases=["clearhistory"])
async def clearsnipehistory(ctx):
    await ctx.message.delete()
    del unknown.snipe_history_dict[ctx.channel.id]
    await ctx.send("Cleared Snipe History of " + ctx.channel.name, delete_after=3)

@unknown.command(aliases=["history"])
async def snipehistory(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in unknown.snipe_history_dict:
        try:
            await ctx.send(unknown.snipe_history_dict[currentChannel])
        except:
            del unknown.snipe_history_dict[currentChannel]
    else:
        await ctx.send("Snipe History is empty!", delete_after=3)
@unknown.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in unknown.sniped_message_dict:
        await ctx.send(unknown.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!", delete_after=3)


@unknown.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in unknown.sniped_edited_message_dict:
        await ctx.send(unknown.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!", delete_after=3)


# FAKE TOKEN GEN      
@unknown.command()
async def tokengen(ctx):
    await ctx.message.delete()
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    first = "".join((random.choice(chars) for i in range(24)))
    second = "".join((random.choice(chars) for i in range(6)))
    third = "".join((random.choice(chars) for i in range(27)))

    await ctx.send(f"""
{first}.{second}.{third}
""")
   
# ADMIN SEVRERS
@unknown.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in unknown.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
            adminPermServers = f"**Servers with Admin ({len(admins)}):**\n```{admins}```"
            botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
            banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
            kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
            await ctx.send(adminPermServers + botPermServers + banPermServers +
                           kickPermServers)    

# BOTS COUNT
@unknown.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace(
                    "_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)


# SAD QUOTE
@unknown.command(name="sadquote", aliases=["sq"])
async def sad_quote(ctx):
    quotes = [
"Sometimes, you have to accept the fact that some people only enter your life as a temporary happiness.",

"The hardest part about walking away from someone is knowing that they won't run after you.",

"The sad truth is that some people are meant to stay in your heart but not in your life.",

"Not all scars show, not all wounds heal. Sometimes you can't see the pain that someone feels.",

"It's sad when you realize you aren't as important to someone as you thought you were.",

"One of the hardest things you will ever have to do is grieve the loss of a person who is still alive.",

"Sometimes, you have to give up on people, not because you don't care, but because they don't.",

"The sad truth is that you can still love someone and be disappointed in them.",

"You can't force someone to care about you. You can only sit and wonder why they don't.",

"Sometimes, the person you want the most is the person you're best without.",

"The saddest thing about betrayal is that it never comes from your enemies, but from those you trust the most.",

"It hurts when you realize you aren't as important to someone as you thought you were.",

"The truth hurts, but the lies are what kill you.",

"The sad truth is that some people will never change, no matter how much you want them to.",

"The deepest wounds are often the ones no one can see.",

"It's sad when you realize you were just a chapter in someone else's story, but they were your whole book.",

"The worst feeling is pretending you don't care about something when it's all you seem to think about.",

"Sometimes, the person who broke you is the only one who can fix you.",

"It's sad how people claim to care about you, but they don't make an effort to stay in your life.",

"The truth is, everyone is going to hurt you. You just have to find the ones worth suffering for.",

"It's sad when you realize you've become an option when you used to be a priority.",

"The saddest kind of sad is when your tears can't even drop and you feel nothing.",

"When you give someone your whole heart and they don't want it, you can't take it back. It's gone forever.",

"The hardest part about walking away from someone is the part where you realize that, no matter how slowly you go, they will never run after you.",

"You can't change how people feel about you, so don't try. Just live your life and be happy.",

"It's sad when you realize that you were worth more than they were willing to give.",

"Sometimes, it's easier to pretend you don't care than to admit that it's killing you.",

"The sad truth is that some people are so used to being hurt that they no longer know what it feels like to be loved.",

"It hurts when you realize you weren't as important to someone as you thought you were.",

"The saddest thing about love is that it's not enough to save someone if they don't want to be saved.",

"The truth is, everyone is going to hurt you. You just have to decide who is worth the pain.",

"It's sad when someone you know becomes someone you knew.",

"The saddest kind of sadness is when you try to explain why you're sad but nothing can come out.",

"You can't make someone feel something they don't, no matter how hard you try.",

"The sad truth is that some people are meant to teach you a lesson, not to be in your life forever.",

"Sometimes, you have to let go of the one you love to find yourself.",

"It's sad when you realize you were just a temporary fix for someone's loneliness.",

"The hardest thing to do is watch the one you love, love someone else.",

"It's sad when you can feel your heart breaking and you can't do anything about it.",

"The truth hurts, but it's better to know than to live in a lie.",

"It's sad when you realize you were never really loved. You were just a convenience.",

"The saddest thing is when you are feeling real down, you look around and realize that there is no shoulder for you.",

"Sometimes, you have to accept that some people are not meant to be in your future.",

"It hurts when you realize you were just an option, not a priority.",

"The sad truth is that some people will only love you as long as you fit into their box.",

"When you lose someone, it's like hearing a loud noise when everything is silent.",

"It's sad when you realize you were the only one putting effort into the relationship.",

"The hardest part of moving forward is not looking back.",

"It's sad when the person who gave you the best memories becomes a memory.",

"The truth is, you can't change someone who doesn't see an issue in their actions.",

"It's sad when you realize you were just a game to someone.",

"The saddest thing is when you're feeling down, you look around, and there's no one there to uplift you."
    ]
    quote = random.choice(quotes)
    await ctx.send(f":broken_heart: {quote}")
    await ctx.message.delete()

# SUPPORT
@unknown.command()
async def support(ctx):
    message = '-  **CONTACT HERE FOR ANY SUPPORT :**\n\n`• INSTAGRAM` **: shyameditzz** \n`• DISCORD`   **: .unknown.4.sure.**\n`• DISCORD SERVER`   **: https://discord.gg/secular**'
    await ctx.send(message)
    await ctx.message.delete()   

# BAN 
@unknown.command(name='banall', aliases=["be", "baneveryone"])
async def ban_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban()
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")

# KICK
@unknown.command(name='kickall', aliases=["ke", "kickeveryone"])
async def kick_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.kick()
            print(f"Kicked {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to kick {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while kicking {m}: {e}")

# DELETE ALL CHANNELS
@unknown.command(name='delchannels', aliases=["dall", "dch"])
async def delete_all_channels(ctx):
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"Deleted {ch}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {ch}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {ch}: {e}")

# SPAM ALL CAHNNELS
@unknown.command(name="spamall", aliases=["sa"])
async def spam_to_all_channels(ctx, amount: int = 50, *, text="@everyone https://discord.gg/secular"):
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(text)
                print(f"Message sent to {ch}")
            except:
                print(f"Can't send message to {ch}")

# DELETE ROLE
@unknown.command(name='deleteroles', aliases=["dr"])
async def delete_all_roles(ctx):
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"Deleted {r}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {r}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {r}: {e}")

# SPAM CHANNELS
@unknown.command(name="spamchannels", aliases=["sch"])
async def spamchannels(ctx, amount: int = 25, *, name="UNKNOWN-RUNS-YOU"):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
            print(f"Created channel")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create channels")
        except discord.HTTPException as e:
            print(f"An error occurred while creating channel: {e}")

# SPAM ROLES
@unknown.command(name="spamroles", aliases=["sr"])
async def spam_with_roles(ctx, amount: int = 25, *, name="SECULAR-OP"):
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name)
            print(f"Created role")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create roles")
        except discord.HTTPException as e:
            print(f"An error occurred while creating role: {e}")

# COPYCAT
@unknown.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    unknown.copycat = user
    await ctx.send("Now copying " + str(unknown.copycat))

# STOP COPY CAT 
@unknown.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if unknown.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(unknown.copycat))
    unknown.copycat = None

# TERRORIST
@unknown.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')
 
# DELETE EMOJIS 
@unknown.command(aliases=["deleteemojis"])
async def delemojis(ctx):
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return 

# DELETE STICKER          
@unknown.command(aliases=["deletestickers"])
async def delstickers(ctx):
   
    for sticker in list(ctx.guild.stickers):
        try:
            await sticker.delete()
        except:
            return 


# CENSOR
@unknown.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')

# UNDERLINE
@unknown.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')

# ITALICIZE
@unknown.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


#TABLE FLIP
@unknown.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

# UNFLIP
@unknown.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

# BOLD
@unknown.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')



# Lenny 
@unknown.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)



# Shrug
@unknown.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

# DICK
@unknown.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): 
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
        await ctx.send(f"{user}'s Dick size 8{dong}D")
        
from bs4 import BeautifulSoup as bs4
# Would You Rather
@unknown.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):  
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"{qa}\nor\n{qb}")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")
    
#CUM
@unknown.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

# LOCK CHANNEL
@unknown.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY LOCKED ', delete_after=deltimer)

# UNLOCK CHANNEL
@unknown.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY UNLOCKED ', delete_after=deltimer)

# HIDE CHANNEL
@unknown.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY HIDE ', delete_after=deltimer)

# UNHIDE CHANNEL 
@unknown.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel:discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + ' SUCCESSFULLY UNHIDE ', delete_after=deltimer)
    
# hypesquad badge
@unknown.command(aliases=["changehypesquad"])
async def hypesquad(ctx, house):
	request = requests.Session()
	headers = {
        'Authorization': Duudu,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
	if house == "bravery":
		payload = {'house_id': 1}
	elif house == "brilliance":
		payload = {'house_id': 2}
	elif house == "balance":
		payload = {'house_id': 3}
	elif house == "random":
		houses = [1, 2, 3]
		payload = {'house_id': random.choice(houses)}
	request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)

# FRY image
@unknown.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_fry.png"))
        except:
            await ctx.send(res['message'])

# MAGIK image
@unknown.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_magik.png"))
        except:
            await ctx.send(res['message'])

# fake tweet image
@unknown.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}"
        ) as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(
                        file=discord.File(file, f"unknown_tweet.png"))
            except:
                await ctx.send(res['message'])

# blur image
@unknown.command()
async def blur(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/blur?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_blur.png"))
        except:
            await ctx.send(endpoint)

# pixelate image
@unknown.command(aliases=["pixel"])
async def pixelate(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_blur.png"))
        except:
            await ctx.send(endpoint)

# supreme image
@unknown.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(
        " ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_supreme.png"))
    except:
        await ctx.send(endpoint)

# dark supreme image
@unknown.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(
        " ", "%20") + "&dark=true"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_dark_supreme.png"))
    except:
        await ctx.send(endpoint)

# fax image
@unknown.command(aliases=["facts"])
async def fax(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(
        " ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_facts.png"))
    except:
        await ctx.send(endpoint)

# BLUR image
@unknown.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_blurpify.png"))
        except:
            await ctx.send(res['message'])

# invert image
@unknown.command()
async def invert(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/invert?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()  
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)

#gay image
@unknown.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)

# communist image
@unknown.command()
async def communist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)
            
# SNOW IMAGE
@unknown.command()
async def snow(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/snow?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)

# JPEG image
@unknown.command(aliases=["jpeg"])
async def jpegify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"unknown_invert.png"))
        except:
            await ctx.send(endpoint)

# pornhub logo image
@unknown.command(aliases=["pornhublogo", "phlogo"])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace(
        "{text-1}", word1).replace("{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)

# PORNHUB COMMENT IMAGE
@unknown.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(
                file=discord.File(file, f"unknown_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])

# MINE SWEEPER GAME
@unknown.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1),
              random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(
                            x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

# TOPIC
@unknown.command()
async def topic(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get(
        'https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)


# massreact
@unknown.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

# DOG
@unknown.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_dog.png"))
    except:
        await ctx.send(link)

# CAT
@unknown.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_cat.png"))
    except:
        await ctx.send(link)

# SAD CAT
@unknown.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_sadcat.png"))
    except:
        await ctx.send(link)

# BIRD
@unknown.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_bird.png"))
    except:
        await ctx.send(link)

# FOX
@unknown.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"unknown_fox.png"))
    except:
        await ctx.send(link)

# uptime
@unknown.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.utcnow(
    )  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)

# SCARPED MSG
@unknown.command()
async def scrapemessages(ctx, number: int):
    channel = ctx.channel

    
    if number <= 0 or number > 10000:
        await ctx.send("Please provide a valid number between 1 and 10,000.")
        return

    
    try:
        messages = []
        async for message in channel.history(limit=number):
            messages.append(f"{message.author}: {message.content}")

        
        content = "\n".join(messages)

        
        with open("scraped-messages.txt", "w", encoding="utf-8") as file:
            file.write(content)

        
        await asyncio.sleep(1)  
        with open("scraped-messages.txt", "rb") as file:
            await ctx.send(file=discord.File(file, filename="scraped-messages.txt"))
    except discord.Forbidden:
        await ctx.send("I don't have permission to access the channel.")
    except discord.HTTPException:
        await ctx.send("An error occurred while fetching messages.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# GIF
@unknown.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get(
            "https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R"
        )
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en"
        )
        res = r.json()
        await ctx.send(res['data'][0]["url"])

# IMAGE SEARCH
@unknown.command(
    aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(
                    f"Search result for: **{args}**",
                    file=discord.File(file, f"unknown_img.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")

# GEN NAME 
@unknown.command(aliases=["fakename"])
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

# CHANNEL SEND ALL
@unknown.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass

# REVAV
@unknown.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        await ctx.send(f"https://images.google.com/searchbyimage?image_url={user.avatar_url}"
        )
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

# QUICK DELETE
@unknown.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)

# 1337 SPEAK
@unknown.command(name='1337speak', aliases=['leetspeak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')    

# DYNO BAN
@unknown.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

# MASS ROLE 
@unknown.command(aliases=[""])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Unknown is daddy", color=randomcolor())
        except:
            return



# UNBAN ALL
@unknown.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

# MEE 6
@unknown.command(aliases=["automee6"])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(
                ctx.message.channel, discord.GroupChannel):
            await ctx.send(
                "You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
            return
        else:
            unknown.mee6 = True
            await ctx.send(
                "Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`",
                delete_after=3)
            unknown.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        unknown.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
    while unknown.mee6 is True:
        sentences = [
            'Stop waiting for exceptional things to just happen.',
            'The lyrics of the song sounded like fingernails on a chalkboard.',
            'I checked to make sure that he was still alive.',
            'We need to rent a room for our party.',
            'He had a hidden stash underneath the floorboards in the back room of the house.',
            'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
            'People generally approve of dogs eating cat food but not cats eating dog food.',
            'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
            'She was the type of girl who wanted to live in a pink house.',
            'The bees decided to have a mutiny against their queen.',
            'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
            'The stranger officiates the meal.',
            'She opened up her third bottle of wine of the night.',
            'They desperately needed another drummer since the current one only knew how to play bongos.',
            'He waited for the stop sign to turn to a go sign.',
            'His thought process was on so many levels that he gave himself a phobia of heights.',
            'Her hair was windswept as she rode in the black convertible.',
            'Karen realized the only way she was getting into heaven was to cheat.',
            'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
            'It was obvious she was hot, sweaty, and tired.',
            'This book is sure to liquefy your brain.',
            'I love eating toasted cheese and tuna sandwiches.',
            'If you don\'t like toenails',
            'You probably shouldn\'t look at your feet.',
            'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
            'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
            'The three-year-old girl ran down the beach as the kite flew behind her.',
            'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
            'They improved dramatically once the lead singer left.',
            'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
            'Excitement replaced fear until the final moment.',
            'The sun had set and so had his dreams.',
            'People keep telling me "orange" but I still prefer "pink".',
            'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
            'I liked their first two albums but changed my mind after that charity gig.',
            'Plans for this weekend include turning wine into water.',
            'A kangaroo is really just a rabbit on steroids.',
            'He played the game as if his life depended on it and the truth was that it did.',
            'He\'s in a boy band which doesn\'t make much sense for a snake.',
            'She let the balloon float up into the air with her hopes and dreams.',
            'There was coal in his stocking and he was thrilled.',
            'This made him feel like an old-style rootbeer float smells.',
            'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
            'The light in his life was actually a fire burning all around him.',
            'Truth in advertising and dinosaurs with skateboards have much in common.',
            'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
            'The view from the lighthouse excited even the most seasoned traveler.',
            'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
            'It\'s difficult to understand the lengths he\'d go to remain short.',
            'Nobody questions who built the pyramids in Mexico.',
            'They ran around the corner to find that they had traveled back in time.'
        ]
        await unknown.get_channel(unknown.mee6_channel).send(
            random.choice(sentences), delete_after=0.1)
        await asyncio.sleep(60)

# READ
@unknown.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in unknown.guilds:
        await guild.ack()

# TOKEN FUCK
@unknown.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type':
        'application/json',
        'Authorization':
            _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Unknown",
        'region': "europe"
    }
    for _i in range(50):
        requests.post(
            'https://discordapp.com/api/v6/guilds',
            headers=headers,
            json=guild)
    while True:
        try:
            request.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings",
                headers=headers,
                json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v6/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@unknown.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

# POLL
@unknown.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(
        arguments[str.find(arguments, "msg:"):str.
                  find(arguments, "1:")]).replace("msg:", "")
    option1 = discord.utils.escape_markdown(
        arguments[str.find(arguments, "1:"):str.
                  find(arguments, "2:")]).replace("1:", "")
    option2 = discord.utils.escape_markdown(
        arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(
        f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')

# 8BALL
@unknown.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    answer = random.choice(responses)
    await ctx.send(f'**This Is My Prediction For Your Question Is This :** `{answer}`')

# SLOT MACHINE
@unknown.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(f"{slotmachine} All matchings, you won!")
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(f"{slotmachine} 2 in a row, you won!")
    else:
        await ctx.send(f"{slotmachine} No match, you lost")

# FIRST MESSAGE
@unknown.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    await ctx.send(f"[Jump]({first_message.jump_url})")

# ABC
@unknown.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

# NUMBERS COUNT
@unknown.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = await ctx.send("Starting count to 100")
    await asyncio.sleep(2)
    for _next in range(100):
        await message.edit(content=_next)
        await asyncio.sleep(2)

# ALL GUILD LEAVE
@unknown.command(aliases=['la'])
async def leaveall(ctx):
 while True:
  for guilds in unknown.guilds:
   try:
    await guilds.leave()
    await ctx.send(f"left {guilds}")
   except:
       await ctx.send(f"couldnt leave {guilds}")

# SINGLE GUILD LEAVE
@unknown.command(aliases=["leaveg","guildleave"])
async def leaveguild(ctx, *, guild: discord.Guild = None):
    #if ctx.author.id in is_bot_owner:
    if guild is None:
        print("Please enter the guild ID!")  # No guild found
        return
    await guild.leave()  # Guild found
    await ctx.send(f"**I left: {guild.name}!**")
    
# ALL GUILDS ID
@unknown.command()
async def guildsid(ctx):
    for guild in unknown.guilds:
            await ctx.send(f"**{guild.name} | {guild.id}**")    

# RANDOM IP
@unknown.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def randomip(ctx):
    octets = [random.randint(0, 255) for forgesb in range(4)]
    forgeip = ".".join(map(str, octets))
    await ctx.reply(f"> **Random IP: {forgeip}**")


#Enable or disable the anti raid option
@unknown.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    unknown.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(
            antiraidparameter).lower() == 'on':
        unknown.antiraid = True
        await ctx.send('- `ANTI-NUKE ENABLED...`')
    elif str(antiraidparameter).lower() == 'false' or str(
            antiraidparameter).lower() == 'off':
        unknown.antiraid = False
        await ctx.send('- `ANTINUKE DISABLED...`')
    else:
        await ctx.send(
            f'- **[! ERROR] ** `USAGE : {unknown.command_prefix}antiraid [true/false]`'
        )


#WWHITE CMD=======================================================================================================================================================================================================
#ADDTION WHITELIST
@unknown.command(aliases=['wl'])
async def whitelist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        await ctx.send(
            f'[ERROR]: USAGE :  {unknown.command_prefix}whitelist <user>')
    else:
        if ctx.guild.id not in unknown.whitelisted_users.keys():
            unknown.whitelisted_users[ctx.guild.id] = {}
        if user.id in unknown.whitelisted_users[ctx.guild.id]:
            await ctx.send("- `" + user.name.replace("*", "\*").replace(
                "`", "\`").replace("_", "\_") + "#" + user.discriminator +
                           "** ALREADY WHITELISTED [!]`")
        else:
            unknown.whitelisted_users[ctx.guild.id][user.id] = 0
            await ctx.send("- `WHITELISTED... " + user.name.replace(
                "*", "\*").replace("`", "\`").replace("_", "\_") + "#" +
                           user.discriminator + "`")


#CHECK WHITELIST
@unknown.command(aliases=['showwl'])
async def whitelisted(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '- `ALL WHITELISTED USERS:`\n'
        for key in unknown.whitelisted_users:
            for key2 in unknown.whitelisted_users[key]:
                user = unknown.get_user(key2)
                whitelist += f'• {user.mention} ({user.id}) IN {unknown.get_guild(key).name}\n'
        await ctx.send(whitelist)
    else:
        whitelist = f'- `WHITELISTED USERS IN {ctx.guild.name}:`\n'
        for key in unknown.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in unknown.whitelisted_users[ctx.guild.id]:
                    user = unknown.get_user(key2)
                    whitelist += f'• {user.mention} ({user.id})\n'

    await ctx.send(whitelist)


#REMOVE FROM WHITELIST
@unknown.command(aliases=['removewl'])
async def unwhitelist(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(
            "- `[ERROR]: SPECIFY TH USER YOU WOULD LIKE TO UNWHITELIST !`")
    else:
        if ctx.guild.id not in unknown.whitelisted_users.keys():
            await ctx.send("- `" + user.name.replace("*", "\*").replace(
                "`", "\`").replace("_", "\_") + "#" + user.discriminator +
                           " IS NOT WHITELISTED`")
            return
        if user.id in unknown.whitelisted_users[ctx.guild.id]:
            unknown.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = unknown.get_user(user.id)
            await ctx.send('- `SUCCESSFULLY UNWHITELISTED' +
                           user2.name.replace('*', "\*").replace(
                               '`', "\`").replace('_', "\_") + '#' +
                           user2.discriminator + '`')


#WHITELIST CLEAR
@unknown.command(aliases=['clearwl', 'clearwld'])
async def clearwhitelist(ctx):
    await ctx.message.delete()
    unknown.whitelisted_users.clear()
    await ctx.send('- `SUCCESFULLY CLEARED WHITELIST')

@unknown.command()
async def category_responder(ctx):
    global command_status
    server_id = SERVER_ID

    if server_id not in command_status:
        command_status[server_id] = False

    command_status[server_id] = not command_status[server_id]
    await ctx.send(
        f'- `CATEGORY RESPONDER IS :  {"ENABLED" if command_status[server_id] else "DISABLED"}`'
    )

# Command: Enable auto-responding feature
@unknown.command()
async def autoresponseenable(ctx):
    unknown.auto_respond_dm_enabled = True
    await ctx.send("- `AUTO-RESPONDING ENABLED`")
    await ctx.message.delete()

# Command: Disable auto-responding feature
@unknown.command()
async def autoresponsedisable(ctx):
    unknown.auto_respond_dm_enabled = False
    await ctx.send("- `AUTO RESPONDING DISABLED`")
    await ctx.message.delete()

# ABUSE
@unknown.command()
async def abuse(ctx):
    message = 'hijarchodh teri mummy ki chut me loda mera teri mumm ki chut aisi marunga behen ke lode gnd chud jayegi teri bhosdike aukat se rahle madarjaat ke pille na to jhaant phadh chudai karunga behenchode rndwwa saala baap se bakchodi pel ra behen ka loda bhosdike teri mummy ki chut maru ghapa ghap ghapa ghap bhosda saala rndi panga na lelio phirse warna ptak ke codh dunga behenchode saale teri maa ka bhosda faad dunga phir wo royegi beth ke behen ki lodi saali chutadi saala chutiyapa karega behen ka loda lund lele baap ka behen ke lodechutadin aale rndwe pille bhosde teri mummy ki chut me loda daalu 10 baar teri mummy chodu 50 baar rndi ke pille aukat na ho to 121 karne ki jurat na ho jai bahin choda saala beta tumhara papa aniket 1021 karke betha hai tum jaiso ko loda chusvata hu behenchodo tumhari mummy ko lund pe jhulata hu saalo rndi ko pillo khandan chud jayega tumhara mujhse 121 karne me behene ke lode mujhse bhidenge'
    await ctx.send(message)
    await ctx.message.delete()
    
# CHAT TRANS
@unknown.command()
async def savetranscript(ctx, filename='transcript.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Chat Transcript for {ctx.channel.name}\n')
            file.write('=' * 40 + '\n\n')

            async for message in ctx.channel.history(limit=None):
                file.write(
                    f'Author: {message.author.name}#{message.author.discriminator} ({message.author.id})\n'
                )
                file.write(f'Time: {message.created_at}\n')
                file.write(f'Content: {message.content}\n')
                file.write('=' * 40 + '\n')

            await ctx.send(f'- `[+] SAVED TO` `{filename}`')
    except Exception as e:
        await ctx.send(f'- `[+] ERROR` {e}')

# ADMIN ALL
@unknown.command()
async def adminall(ctx):
    await ctx.message.delete()
    try:
        role = discord.utils.get(ctx.guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
    except:
        pass

#############################################################################################################################################################################


@unknown.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO  is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.send('owoh')
            await ctx.send('owob')
            await asyncio.sleep(15)
            
            
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)

@unknown.command(pass_context=True)
async def startowo(ctx):
    await ctx.message.delete()
    await ctx.send('**OWO STARTED**')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await ctx.send('<@974191304911233054> Break of 5 Min')
            await asyncio.sleep(300)
          
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(4)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await ctx.send('<@974191304911233054> Break of 15 Min')
            await asyncio.sleep(900)

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(4)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await ctx.send('<@974191304911233054> Break of 15 Min')
            await asyncio.sleep(900)
          
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await ctx.send('<@974191304911233054> Break of 15 Min')
            await asyncio.sleep(1200)     

@unknown.command()
async def stopowo(ctx):
    await ctx.message.delete()
    await ctx.send('**OWO STOPED**')
    global dmcs
    dmcs = False
################################################################################################################################################

# MODERATOR COMMANDS

@unknown.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason=reason)

@unknown.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.kick(reason=reason)

@unknown.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member:discord.Member, role:discord.Role):
    await ctx.message.delete()
    await member.add_roles(role)

@unknown.command()
@commands.has_permissions(manage_roles=True)
async def takerole(ctx, member:discord.Member, role:discord.Role):
    await ctx.message.delete()
    await member.remove_roles(role)


@unknown.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        unknown.msgsniper = True
        await ctx.send(f'{unknown.user.name}Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        unknown.msgsniper = False
        await ctx.send(f'{unknown.user.name}Message-Sniper is now **disabled**')


@unknown.command()
async def fnuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(".unknown.4.sure.")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    amount = 5
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 7, max_uses = 25)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_MESSAGE))
    print(f"nuked {guild.name} Successfully.")
    return

@unknown.command()
async def nukestop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{unknown.user.name} has logged out successfully." + Fore.RESET)


@unknown.command()
@commands.has_permissions(manage_roles=True)
async def client(ctx, member: discord.Member):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, id=1197230356189954098)
    await member.add_roles(role)
    await ctx.send(f'**{member.mention} Has Been Given Client Role.**')


@unknown.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
  await ctx.message.delete()
  await unknown.create_guild(f'backup-{ctx.guild.name}')
  await asyncio.sleep(4)
  for g in unknown.guilds:
    if f'backup-{ctx.guild.name}' in g.name:
      for c in g.channels:
        await c.delete()
      for cate in ctx.guild.categories:
        x = await g.create_category(f"{cate.name}")
        for chann in cate.channels:
          if isinstance(chann, discord.VoiceChannel):
            await x.create_voice_channel(f"{chann}")
          if isinstance(chann, discord.TextChannel):
            await x.create_text_channel(f"{chann}")
  try:
    await g.edit(icon=ctx.guild.icon_url)
  except:
    pass

@unknown.command()
async def dmlist(ctx, *, x):
    await ctx.message.delete()
    for channel in unknown.private_channels:
        try:
            await channel.send(x)
            print(f"DMd {channel}")
        except:
            print(f"Can't DM {channel}")
            continue
        
@unknown.command()
async def level(ctx):
    await ctx.message.delete()
    responses = [
        'Cry about it', 'Cartier the best coder', 'We love you tecca',
        'Shiver me timbers', 'Cartier the skid 🥶', 'Shut the up'
    ]
    answer = random.choice(responses)
    await ctx.send(answer)
    await asyncio.sleep(5)


@unknown.command()
async def addar(ctx, trigger, *, response):
    autoresponder_data = load_autoresponder_data()
    autoresponder_data[trigger] = response
    save_autoresponder_data(autoresponder_data)
    await ctx.send(f'Autoresponder added: `{trigger}` -> `{response}`')

@unknown.command()
async def removear(ctx, trigger):
    autoresponder_data = load_autoresponder_data()
    if trigger in autoresponder_data:
        del autoresponder_data[trigger]
        save_autoresponder_data(autoresponder_data)
        await ctx.send(f'Autoresponder removed: `{trigger}`')
    else:
        await ctx.send('Autoresponder not found.')

@unknown.command()
async def listar(ctx):
    autoresponder_data = load_autoresponder_data()
    if autoresponder_data:
        response = 'Autoresponders:\n'
        for trigger, response_text in autoresponder_data.items():
            response += f'`{trigger}` -> `{response_text}`\n'
        await ctx.send(response)
    else:
        await ctx.send('No autoresponders found.')


@unknown.command(aliases=['info', 'stats'])
async def selfbot(ctx):
    version = "UNKNOWN V1"
    language = "Python"
    author = "U N K N O W N"
    total_commands = len(unknown.commands)
    server_link = "https://discord.gg/secular"

    
    ram_info = psutil.virtual_memory()
    total_ram = round(ram_info.total / (1024 ** 3), 2)  
    used_ram = round(ram_info.used / (1024 ** 3), 2)  

    
    os_info = platform.platform()

    message = f"**__UNKNOWN S3LFB0T__**\n\n" \
              f"**• Vers: {version}\n" \
              f"• Lang: {language}\n" \
              f"• Created By: {author}\n" \
              f"• Total Cmds: {total_commands}\n" \
              f"• Used RAM: {used_ram} GB\n" \
              f"• Total RAM: {total_ram} GB\n" \
              f"• Operating System: {os_info}\n\n" \
              f"• Server: {server_link} **"

    await ctx.send(message)
  
@unknown.command()
async def mm(ctx, arg, args):
    await ctx.reply('`+vouch <@924616449715212368> LEGIT MM | HOLD '+ arg + ' FOR '+ args + ' ✓ `')
    await ctx.send('Thank You For Using Unknown Service Pls Vouch Me On https://discord.gg/secular')

@unknown.command()
async def exch(ctx, arg, args):
    await ctx.reply('`+vouch <@924616449715212368> LEGIT EXCH | '+ arg + ' TO '+ args + ' ✓ `')
    await ctx.send('Thank You For Using Unknown Service Pls Vouch Me On https://discord.gg/secular')

@unknown.command()
async def sold(ctx, arg, args):
    await ctx.reply('`+vouch <@924616449715212368> LEGIT BOUGHT  '+arg + ' FOR '+ args + '  ✓ `')
    await ctx.send('Thank You For Using Unknown Service Pls Vouch Me On https://discord.gg/secular')


@unknown.command(aliases=['am'])
async def automessage(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Please provide the channel ID for the auto message:")
    await asyncio.sleep(2)  
    try:
        channel_id_msg = await unknown.wait_for('message', check=check, timeout=30)
        channel_id = int(channel_id_msg.content)
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")
    except ValueError:
        return await ctx.send("Invalid channel ID. Please try again.")

    await ctx.send("Please provide the interval (in seconds) between messages:")
    await asyncio.sleep(2)  
    try:
        interval_msg = await unknown.wait_for('message', check=check, timeout=30)
        interval = int(interval_msg.content)
        if interval < 5:
            return await ctx.send("Interval should be at least 5 seconds.")
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")
    except ValueError:
        return await ctx.send("Invalid interval. Please try again.")

    await ctx.send("Please provide the number of times to send the message:")
    await asyncio.sleep(2)  
    try:
        count_msg = await unknown.wait_for('message', check=check, timeout=30)
        count = int(count_msg.content)
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")
    except ValueError:
        return await ctx.send("Invalid count. Please try again.")

    await ctx.send("Please provide the message content:")
    await asyncio.sleep(2)  
    try:
        message = await unknown.wait_for('message', check=check, timeout=30)
        message_content = message.content
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")

    task_id = str(uuid.uuid4())
    if len(auto_messages) >= 3:
        return await ctx.send("Maximum limit for auto messages reached.")
    else:
        auto_messages[task_id] = {
            'channel_id': channel_id,
            'message': message_content,
            'interval': interval,
            'count': count,
            'next_run': asyncio.get_event_loop().time() + interval
        }
        await ctx.send(f"Auto message with ID: {task_id} set successfully.")

@unknown.command()
async def listauto(ctx):
    if auto_messages:
        for task_id, task_data in auto_messages.items():
            channel = unknown.get_channel(task_data['channel_id'])
            remaining_time = task_data['next_run'] - asyncio.get_event_loop().time()
            await ctx.send(f"**Task ID** \n⇁{task_id} \n\n**Channel** \n⇁{channel.name if channel else 'Unknown'} \n\n**Interval** \n⇁{task_data['interval']}s \n\n**Count** \n⇁{task_data['count']} \n\n**Remaining Time** \n⇁{remaining_time:.2f}s \n\n**Message** \n⇁{task_data['message']}\n\n")
    else:
        await ctx.send("No auto messages currently set.")

@unknown.command(aliases=['sam'])
async def stopauto(ctx, task_id: str):
    if task_id in auto_messages:
        del auto_messages[task_id]
        await ctx.send(f"Auto message with ID: {task_id} stopped successfully.")
    else:
        await ctx.send(f"Auto message with ID: {task_id} not found.")

async def send_auto_message(task_id, channel_id, message):
    channel = unknown.get_channel(channel_id)
    if channel:
        await channel.send(message)
    auto_messages[task_id]['count'] -= 1
    auto_messages[task_id]['next_run'] = asyncio.get_event_loop().time() + auto_messages[task_id]['interval']


@unknown.command(aliases=['247'])
async def connectvc(ctx, channel_id):
    try:
        channel = unknown.get_channel(int(channel_id))

        if channel is None:
            return await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")

        if isinstance(channel, discord.VoiceChannel):
            permissions = channel.permissions_for(ctx.guild.me)

            if not permissions.connect or not permissions.speak:
                return await ctx.send("I don't have permissions to connect or speak in that channel.")

            voice_channel = await channel.connect()
            await ctx.send(f"Connected to voice channel: {channel.name}")

            await channel.send("Hello, I have connected to this voice channel!")

        else:
            await ctx.send("This is not a voice channel. Please provide a valid voice channel ID.")
    except discord.errors.ClientException:
        await ctx.send("I'm already connected to a voice channel.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to perform this action.")
    except ValueError:
        await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@unknown.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    await ctx.send(final_str)
    
@unknown.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])
    
    
@unknown.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in unknown.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in unknown.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )
            
            
@unknown.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()
    
    
@unknown.command()
async def upi_id(ctx):
    await ctx.message.delete()
    await ctx.send(f'{UPI}') 
       
@unknown.command()
async def upi_qr(ctx):
    await ctx.message.delete()
    await ctx.send(f'{UPI_QR}') 

@unknown.command()
async def ltc_id(ctx):
    await ctx.message.delete()
    await ctx.send(f'{LTC}') 

@unknown.command()
async def ltc_qr(ctx):
    await ctx.message.delete()
    await ctx.send(f'{LTC_QR}') 

@unknown.command()
async def btc_id(ctx):
    await ctx.message.delete()
    await ctx.send(f'{BTC}')

@unknown.command()
async def btc_qr(ctx):
    await ctx.message.delete()
    await ctx.send(f'{BTC_QR}')
    
@unknown.command()
async def eth_id(ctx):
    await ctx.message.delete()
    await ctx.send(f'{ETH}')

@unknown.command()
async def eth_qr(ctx):
    await ctx.message.delete()
    await ctx.send(f'{ETH_QR}')
    
@unknown.command()
async def paypal(ctx):
    await ctx.message.delete()
    await ctx.send(f'{PayPal}')


# TRIVIA
@unknown.command(name='trivia', help='Get a random trivia question')
async def trivia(ctx):
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()
    
    question = data['results'][0]['question']
    correct_answer = data['results'][0]['correct_answer']
    options = data['results'][0]['incorrect_answers'] + [correct_answer]
    
    random.shuffle(options)
    formatted_options = '\n'.join([f"{chr(65 + i)}. {option}" for i, option in enumerate(options)])
    
    trivia_message = f"**Trivia Question:**\n{question}\n\n**Options:**\n{formatted_options}"
    
    await ctx.send(trivia_message)

    await asyncio.sleep(5)
    
    await ctx.send(f"**The correct answer is: `{correct_answer}`**")




@unknown.command(name='find', help='Find all messages containing a keyword')
async def find(ctx, keyword):
    try:
        for guild in unknown.guilds:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).read_messages:
                    async for message in channel.history(limit=300):
                        if keyword.lower() in message.content.lower():
                            user_info = f"{message.author.name}#{message.author.discriminator} ({message.author.id})"
                            await ctx.send(f"Found in {guild.name} > {channel.name}:\n"
                                           f"User: {user_info}\n"
                                           f"Message: `{message.content}`")
    except Exception as e:
        error_message = f"An error occurred: {type(e).__name__} - {e}"
        print(error_message)
        await ctx.send(error_message)
        


@unknown.command()
async def define(ctx, *, word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            word_data = data[0]
            word_meanings = word_data['meanings']
            
            meanings_list = []
            for meaning in word_meanings:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                
                def_text = f"**{part_of_speech.capitalize()}:**\n"
                for i, definition in enumerate(definitions, start=1):
                    def_text += f"{i}. {definition['definition']}\n"
                    if 'example' in definition:
                        def_text += f"   *Example: {definition['example']}*\n"
                
                meanings_list.append(def_text)
            
            result_text = f"**{word.capitalize()}**\n\n" + '\n'.join(meanings_list)
            await ctx.send(result_text)
        else:
            await ctx.send("No definitions found for that word.")
    else:
        await ctx.send("Failed to retrieve the word definition.")
     


@unknown.command()
async def bin(ctx, bin_number: str):
    url = f"https://lookup.binlist.net/{bin_number}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "bank" in data:
            issuer = data["bank"]["name"]
        else:
            issuer = "Unknown"

        if "country" in data:
            country = data["country"]["name"]
        else:
            country = "Unknown"

        await ctx.send(f"Issuer: {issuer}\nCountry: {country}")
    else:
        await ctx.send("Invalid BIN or an error occurred.")


@unknown.command()
async def addstock(ctx, stock: str, filename: str):
    # Open the text file in append mode and write the stock value on a new line
    with open(filename, 'a') as file:
        file.write(stock + '\n')
    await ctx.send(f'Stock "{stock}" has been added to {filename}.')

@unknown.command()
async def getstock(ctx, amount: int):
    # Read the text file and retrieve the specified number of stock items
    with open('stock.txt', 'r') as file:
        stocks = file.read().splitlines()
    if amount > len(stocks):
        await ctx.send('Not enough stock available.')
    else:
        selected_stocks = stocks[:amount]
        await ctx.send('\n'.join(selected_stocks))

@unknown.command()
async def deletestock(ctx):
    # Delete the entire stock by truncating the file
    with open('stock.txt', 'w') as file:
        file.truncate()
    await ctx.send('All stock items have been deleted.')  

# API endpoint for math calculations
api_endpoint = 'https://api.mathjs.org/v4/'
@unknown.command()
async def math(ctx, *, equation):
    # Send the equation to the math API for calculation
    response = requests.get(api_endpoint, params={'expr': equation})

    if response.status_code == 200:
        result = response.text
        await ctx.send(f'Result: {result}')
    else:
        await ctx.send('Failed to calculate the equation.')

@unknown.command()
async def searchmath(ctx, *, query):
    # Create the Google search query
    search_query = f'{query} math solutions'

    # Perform the Google search and get the top three results
    search_results = search(search_query, num_results=3)

    # Prepare the response message
    message = 'Top 3 math solutions:\n'
    for index, result in enumerate(search_results, start=1):
        message += f'{index}. {result}\n'

    # Send the response message
    await ctx.send(message)

@unknown.command()
async def capmonster(ctx, api_key):
    response = requests.post('https://api.capmonster.cloud/getBalance', json={
        'clientKey': api_key
    })
    if response.status_code == 200:
        balance = response.json()['balance']
        await ctx.send(f'[ + ] Capmonster API Key Balance : ${balance}.Credits - Unknown')
    else:
        await ctx.send('[ - ] Invalid API key provided.Credits - Unknown')
        
@unknown.command()
async def hotmailbox(ctx, api_key):
    response = requests.get(f'https://api.hotmailbox.me/user/balance?apikey={api_key}')
    if response.status_code == 200:
        response_json = response.json()
        if 'BalanceUsd' in response_json:
            balance_usd = response_json['BalanceUsd']
            await ctx.send(f'[ + ] Hotmailbox API Key Balance : ${balance_usd}')
        else:
            await ctx.send('[ - ] Invalid API key provided.Credits - Unknown')
    else:
        await ctx.send('[ - ] Invalid API key provided.-Credits Unknown')

@unknown.command()
async def kopeechka(ctx, api_key):
    response = requests.get(f'https://api.kopeechka.store/user-balance?token={api_key}&type=json&api=2.0')
    if response.status_code == 200:
        response_json = response.json()
        if 'balance' in response_json:
            balance = response_json['balance']
            await ctx.send(f'[ + ] Kopeechka API Key Balance : {balance} Credits - Unknown ')
        else:
            await ctx.send('[ - ] Invalid API key provided.- Credits Unknown')
    else:
        await ctx.send('[ - ] Invalid API key provided.')
        
@unknown.command()
async def gen(ctx, bin, amount):
    # Check if the amount is valid
    try:
        amount = int(amount)
        if amount < 1 or amount > 3000:
            raise ValueError
    except ValueError:
        await ctx.send("Please provide a valid amount between 1 and 3000.")
        return

    # Generate and validate card details
    cards = []
    for _ in range(amount):
        card = list(bin)
        while len(card) < 16:
            digit = random.choice("0123456789")
            card.append(digit)
        luhn_sum = 0
        for i, digit in enumerate(reversed(card)):
            if i % 2 == 0:
                double = int(digit) * 2
                if double > 9:
                    double -= 9
                luhn_sum += double
            else:
                luhn_sum += int(digit)
        checksum = (luhn_sum * 9) % 10
        card.append(str(checksum))

        # Generate random expiry month, expiry year, and CVV
        expiry_month = str(random.randint(1, 12)).zfill(2)
        expiry_year = str(random.randint(23, 30)).zfill(2)
        cvv = str(random.randint(100, 999)).zfill(3)

        card_details = "|".join(["".join(card), expiry_month, expiry_year, cvv])
        cards.append(card_details)

    # Save card details to a text file
    filename = f"{bin}_{amount}_cards.txt"
    with open(filename, "w") as file:
        file.write("\n".join(cards))

    # Send the text file to Discord
    await ctx.send(file=discord.File(filename)) 

@unknown.command()
async def system_info(ctx):
    disk_usage = psutil.disk_usage('/')
    cpu_info = psutil.cpu_percent(interval=1, percpu=True)
    disk_partitions = psutil.disk_partitions()

    # Disk usage
    total_disk_space = f"Total disk space: {disk_usage.total / (1024**3):.2f} GB"
    used_disk_space = f"Used disk space: {disk_usage.used / (1024**3):.2f} GB"
    free_disk_space = f"Free disk space: {disk_usage.free / (1024**3):.2f} GB"
    disk_usage_percentage = f"Disk usage percentage: {disk_usage.percent}%"

    # CPU info
    cpu_info_str = '\n'.join(f"CPU {i}: {usage}%" for i, usage in enumerate(cpu_info))

    # Disk info
    disk_info_str = '\n'.join(f"Device: {partition.device}, Mountpoint: {partition.mountpoint},"
                              f" Filesystem: {partition.fstype}" for partition in disk_partitions)

    response = f"{total_disk_space}\n{used_disk_space}\n{free_disk_space}\n{disk_usage_percentage}\n\n" \
               f"{cpu_info_str}\n\n{disk_info_str}"

    await ctx.send(response)  
startup_time = datetime.now()

@unknown.command()
async def news(ctx):
    # Make a request to the news API to fetch the latest news articles
    url = "https://newsapi.org/v2/top-headlines"
    parameters = {
        "apiKey": "4d928f2f2c7d4430868a29e5be4d6a90",  # Replace with your own News API key
        "language": "en",
        "pageSize": 5,  # Specify the number of articles you want to fetch
    }
    response = requests.get(url, params=parameters)
    news_data = response.json()

    # Process the response and send the news articles as a response
    if news_data["status"] == "ok":
        articles = news_data["articles"]
        for article in articles:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            await ctx.send(f"**{title}**\n{description}\nRead more: {url}")
    else:
        await ctx.send("Failed to fetch news.")
        
@unknown.command()
async def gitsearch(ctx, repository_name: str):
    try:
        # Search for repositories on GitHub
        url = f"https://api.github.com/search/repositories?q={repository_name}"
        response = requests.get(url)
        data = response.json()

        # Process the response and send repository information as a response
        if "items" in data:
            repositories = data["items"][:5]  # Limit the number of repositories to display
            for repository in repositories:
                repo_name = repository["full_name"]
                repo_url = repository["html_url"]
                await ctx.send(f"**Repository:** {repo_name}\n{repo_url}")
        else:
            await ctx.send("No repositories found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
        
@unknown.command()
async def gituser(ctx, username: str):
    api_url = f"https://api.github.com/users/{username}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        user_data = response.json()
        
        message = f"**GitHub User Information**\n\n"
        message += f"**Username:** {user_data['login']}\n"
        message += f"**Name:** {user_data['name'] or 'Not specified'}\n"
        message += f"**Bio:** {user_data['bio'] or 'Not specified'}\n"
        message += f"**Followers:** {user_data['followers']}\n"
        message += f"**Following:** {user_data['following']}\n"
        message += f"**Public Repositories:** {user_data['public_repos']}\n"
        message += f"**GitHub URL:** {user_data['html_url']}\n"
        
        await ctx.send(message)
    elif response.status_code == 404:
        await ctx.send("User not found.")
    else:
        await ctx.send("Failed to fetch user information.")

@unknown.command()
async def rndaddress(ctx):
    # Make a request to the Random User Generator API
    response = requests.get('https://randomuser.me/api/')
    data = response.json()

    # Extract the address information from the API response
    address_info = data['results'][0]['location']

    # Use Faker to generate a random name for testing purposes
    fake_name = fake.name()

    # Format the address information
    address = f'{fake_name}\n{address_info["street"]["number"]} {address_info["street"]["name"]}\n{address_info["city"]}, {address_info["state"]}, {address_info["country"]} {address_info["postcode"]}'

    # Send the generated address as a reply
    await ctx.send(address)

@unknown.command()
async def nsfwwaifu(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/waifu")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")
        
@unknown.command()
async def nsfwneko(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/neko")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")
        
@unknown.command()
async def nsfwtrap(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/trap")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")

@unknown.command()
async def channelinfo(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    channel_id = channel.id
    channel_name = channel.name
    channel_topic = channel.topic or "No topic set"
    response = f"Channel ID: {channel_id}\nChannel Name: {channel_name}\nChannel Topic: {channel_topic}"
    await ctx.send(response)
    
unsplash_access_key = 's8neBEpVxPxjyCq4K0K-v8c9Db9Oym2FijXWyCcNij0'
@unknown.command()
async def findphoto(ctx, location):
    # Set up the API request to Unsplash
    url = 'https://api.unsplash.com/photos/random'
    headers = {'Authorization': f'Client-ID {unsplash_access_key}'}
    params = {'query': location, 'orientation': 'landscape'}

    # Send the API request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data and 'urls' in data and 'regular' in data['urls']:
            photo_url = data['urls']['regular']
            await ctx.send(photo_url)
        else:
            await ctx.send("Sorry, I couldn't find a photo for that location.")
    else:
        await ctx.send("An error occurred while fetching the photo.")
        
google_api_key = 'AIzaSyDqk7JHB56dMBW8Fmd0kYG6d98-GSAf6k0'
search_engine_id = '80db58308412546d9'
@unknown.command()
async def photosearch(ctx, *, query):
    # Set up the API request to Google CSE
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': google_api_key,
        'cx': search_engine_id,
        'q': query,
        'searchType': 'image',
        'num': 1  # Number of results to retrieve (change as needed)
    }

    # Send the API request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            image_url = data['items'][0]['link']
            await ctx.send(image_url)
        else:
            await ctx.send("Sorry, I couldn't find any photos for that query.")
    else:
        await ctx.send("An error occurred while fetching the photos.")


@unknown.command()
async def base64encode(ctx, *, message):
    encoded_message = base64.b64encode(message.encode()).decode()
    await ctx.send(f'Base64 Encoded: {encoded_message}')

@unknown.command()
async def base64decode(ctx, *, encoded_message):
    try:
        decoded_message = base64.b64decode(encoded_message).decode()
        await ctx.send(f'Base64 Decoded: {decoded_message}')
    except base64.binascii.Error:
        await ctx.send('Invalid Base64 encoded message.')
        
api_key = '7f37c925-57ab-bb63-ef54-fd52bb201d54:fx'  
@unknown.command()
async def translate(ctx, source_lang, target_lang, *, text):
    try:
        headers = {
            'Authorization': f'DeepL-Auth-Key {api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'text': text,
            'source_lang': source_lang,
            'target_lang': target_lang
        }
        response = requests.post('https://api-free.deepl.com/v2/translate', headers=headers, data=payload)
        translation_data = response.json()
        translated_text = translation_data['translations'][0]['text']

        translation_message = (
            f"**Translation**\n"
            f"Source Language: {source_lang}\n"
            f"Target Language: {target_lang}\n"
            f"Source Text: {text}\n"
            f"Translated Text: {translated_text}"
        )

        await ctx.send(translation_message)
    except KeyError:
        await ctx.send("Translation failed. Please check your language codes or try again later.")
        
@unknown.command()
async def mapsearch(ctx, *, location):
    # Construct the API request URL
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"

    headers = {'User-Agent': '.unknown.4.sure.'}

    # Make a GET request to the OpenStreetMap API
    response = requests.get(url, headers=headers)
    data = response.json()

    if len(data) > 0:
        # Get the first result
        result = data[0]
        
        # Get the formatted address and location
        formatted_address = result['display_name']
        lat = result['lat']
        lon = result['lon']

        # Create a text message with the information
        message = f"**OpenStreetMap Search Result**\n\n**Address:** {formatted_address}\n**Coordinates:** Latitude: {lat}, Longitude: {lon}"
        
        # Send the message to the channel
        await ctx.send(message)
    else:
        await ctx.send(f"No results found for '{location}'.")

@unknown.command()
async def weather(ctx, *, city: str):
    api_key = "c9f448f65cda132e2f1c4ca0ea2667aa"  # Replace with your OpenWeatherMap API Key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']

        await ctx.send(f"Temperature : {temperature} \nHumidity : {humidity}% \nPressure : {pressure} hPa \nDescription : {weather_report[0]['description']}")
    else:
        await ctx.send("City Not Found!")

@unknown.command()
async def copyserver2(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = unknown.get_guild(source_guild_id)
    target_guild = unknown.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("One of the guilds wasn't found!")
        return

    # Clone roles from source to target
    roles = sorted(source_guild.roles, key=lambda role: role.position)

    for role in roles:
        if role.name != "@everyone":
            await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
            await ctx.send(f"Role {role.name} has been created on the target guild.")
            await asyncio.sleep(5) #Add delay here

    # Clone channels from source to target
    text_channels = sorted(source_guild.text_channels, key=lambda channel: channel.position)
    voice_channels = sorted(source_guild.voice_channels, key=lambda channel: channel.position)

    for channel in text_channels:
        await target_guild.create_text_channel(name=channel.name)
        await ctx.send(f"Text Channel {channel.name} has been created on the target guild.")
        await asyncio.sleep(5)  # Add delay here

    for channel in voice_channels:
        await target_guild.create_voice_channel(name=channel.name)
        await ctx.send(f"Voice Channel {channel.name} has been created on the target guild.")
        await asyncio.sleep(5)  # Add delay here


forced_nicks = {}
@unknown.command(name='forcenick', aliases=['fucknick','fn'], brief="Force a users nickname", usage=".forcenick <mention.user> <nick.name>")
@commands.has_permissions(manage_nicknames=True)
async def forcenick(ctx, user: discord.Member, *, nickname: str):
    forced_nicks[user.id] = nickname
    try:
        await user.edit(nick=nickname)
        await ctx.send(f"Fucked nickname '{nickname}' on {user.display_name}.")
    except discord.Forbidden:
        await ctx.send("I dont have perms to edit nn")

@unknown.command(name='stopforcenick', aliases=['sfn','stopfucknick'], brief="Stop force kicking the user", usage=".stopforcenick <mention.user>")
@commands.has_permissions(manage_nicknames=True)
async def stopforcenick(ctx, user: discord.Member):
    if user.id in forced_nicks:
        del forced_nicks[user.id]
        try:
            await user.edit(nick=None)
            await ctx.send(f"Stopped fucking nickname on {user.display_name}.")
        except discord.Forbidden:
            await ctx.send("I dont have perms to edit nn")
    else:
        await ctx.send(f"No forced nickname found for {user.display_name}.")

@unknown.event
async def on_member_update(before, after):
    if after.id in forced_nicks and after.nick != forced_nicks[after.id]:
        try:
            await after.edit(nick=forced_nicks[after.id])
        except discord.Forbidden:
            pass

@forcenick.error
async def forcenick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have 'Manage Nicknames' perms")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid user or nickname provided.")
    else:
        await ctx.send("An error occurred while executing the command.")

@stopforcenick.error
async def stopforcenick_error(ctx, error):
    """Error handler for stopforcenick command."""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have 'Manage Nicknames' perms to use this cmd")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid user provided.")
    else:
        await ctx.send("An error occurred while executing the command.")


@unknown.command()
async def screenshot(ctx, url):
    api_ba = '0c8733' # Replace with your API Key
    endpoint = 'https://api.screenshotmachine.com'
    
    params = {
        'key': api_ba,
        'url': url,
        'dimension': '1024xfull', # choose a dimension you prefer
        'format': 'png',
        'cacheLimit': '0',
        'timeout': '200'
    }
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        with open('screenshot.png', 'wb') as f:
            f.write(response.content)

        await ctx.send(file=discord.File('screenshot.png'))
        os.remove('screenshot.png') # remove the file after sending it
    else:
        await ctx.send('Failed to take screenshot.')
        
API_LOL = 'AIzaSyDqk7JHB56dMBW8Fmd0kYG6d98-GSAf6k0'
CX_ID = '80db58308412546d9'
@unknown.command()
async def gimage(ctx, *, query: str):
    """Search for an image on Google."""
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': API_LOL,
        'cx': CX_ID,
        'q': query,
        'searchType': 'image',
        'num': 1
    }
    response = requests.get(url, params=params).json()
    try:
        image_url = response['items'][0]['link']
        await ctx.send(image_url)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@unknown.command()
async def joinsrv(ctx, invite_link: str, token: str):
    code = gi_code(invite_link)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token.strip('\"'),  # Remove surrounding double quotes from token
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wKChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com',
        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}) as resp:
            if resp.status == 200:
                await ctx.send("Joined successfully")
            elif resp.status == 429:
                j = await resp.json()
                await ctx.send(f"Ratelimited for {j['retry_after']} seconds")
                await asyncio.sleep(j['retry_after'])
            elif resp.status == 403:
                await ctx.send("Locked token")
            else:
                j = await resp.json()
                await ctx.send(f"Failed to join the server. Error: {j}")
                return

async def aprint(text):
    print(text)

def gi_code(link):
    if link.startswith("https://discord.gg/"):
        return link[19:]
    elif link.startswith(".gg/"):
        return link[4:]
    else:
        return link   

API_XD = "9bd8c64f65124903b9129d2d52a5d130"  # Replace with your NewsAPI key
@unknown.command()
async def footballnews(ctx):
    url = f"https://newsapi.org/v2/top-headlines?q=football&apiKey={API_XD}"
    response = requests.get(url)
    news_data = response.json()

    for article in news_data['articles']:
        title = article['title']
        description = article['description']
        source = article['source']['name']
        url = article['url']
        
        message = f"**{title}**\n{description}\nSource: {source}\nRead More: {url}"
        await ctx.send(message)
        
API_ASS = "K84396224988957"
@unknown.command()
async def readtext(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image.")
        return

    image_url = ctx.message.attachments[0].url

    try:
        payload = {
            "url": image_url,
            "apikey": API_ASS
        }

        response = requests.post("https://api.ocr.space/parse/image", data=payload)
        result = response.json()

        if result["IsErroredOnProcessing"]:
            await ctx.send("Error occurred during image processing.")
        elif result["ParsedResults"]:
            text = result["ParsedResults"][0]["ParsedText"]
            await ctx.send(text)
        else:
            await ctx.send("No text found in the image.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@unknown.command()
async def listfilters(ctx):
    filters = ['BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES',
               'SHARPEN', 'SMOOTH', 'SMOOTH_MORE']
    await ctx.send("Available filters: " + ', '.join(filters))

@unknown.command()
async def resizeimage(ctx, dimensions: str):
    # Check if an image is attached to the message
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image to resize.")
        return

    # Get the first attached image
    attachment = ctx.message.attachments[0]

    # Check if the attached file is an image
    if not attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        await ctx.send("Invalid image format. Please provide a PNG, JPEG, or GIF image.")
        return

    # Download the image
    response = await attachment.read()
    image = Image.open(BytesIO(response))

    # Parse the dimensions
    try:
        width, height = map(int, dimensions.split('*'))
    except ValueError:
        await ctx.send("Invalid dimensions. Please provide the width and height in the format 'width*height'.")
        return

    # Resize the image
    resized_image = image.resize((width, height))

    # Save the resized image to a BytesIO buffer
    resized_image_buffer = BytesIO()
    resized_image.save(resized_image_buffer, format='PNG')
    resized_image_buffer.seek(0)

    # Send the resized image as a response
    resized_image_file = discord.File(resized_image_buffer, filename="resized_image.png")
    await ctx.send(file=resized_image_file)
    
@unknown.command()
async def applyfilter(ctx, filter_name: str):
    # Check if an image is attached to the message
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image to apply the filter.")
        return

    # Get the first attached image
    attachment = ctx.message.attachments[0]

    # Check if the attached file is an image
    if not attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        await ctx.send("Invalid image format. Please provide a PNG, JPEG, or GIF image.")
        return

    # Download the image
    response = await attachment.read()
    image = Image.open(BytesIO(response))

    # Apply the filter
    filter_name = filter_name.upper()
    if hasattr(ImageFilter, filter_name):
        filtered_image = image.filter(getattr(ImageFilter, filter_name))
    else:
        await ctx.send("Invalid filter name. Use `.listfilters` to see available filters.")
        return

    # Save the filtered image to a BytesIO buffer
    filtered_image_buffer = BytesIO()
    filtered_image.save(filtered_image_buffer, format='PNG')
    filtered_image_buffer.seek(0)

    # Send the filtered image as a response
    filtered_image_file = discord.File(filtered_image_buffer, filename="filtered_image.png")
    await ctx.send(file=filtered_image_file)



@unknown.command()
async def recentgames(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = f'https://api.football-data.org/v2/matches'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching recent games: {err}")
        return

    data = response.json()
    matches = data.get("matches", [])
    if not matches:
        await ctx.send("No recent football games found.")
        return

    game_list = []
    for match in matches:
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        score_home = match["score"]["fullTime"]["homeTeam"]
        score_away = match["score"]["fullTime"]["awayTeam"]
        status = match["status"]
        game_list.append(f"{home_team} vs {away_team}: {score_home}-{score_away} ({status})")

    await ctx.send("Recent Football Games:\n" + "\n".join(game_list))
    
@unknown.command()
async def premiertable(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = 'https://api.football-data.org/v2/competitions/PL/standings'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching Premier League table: {err}")
        return

    data = response.json()
    standings = data.get("standings", [])
    if not standings:
        await ctx.send("No Premier League table found.")
        return

    table = standings[0]["table"]
    table_lines = []
    for position, team in enumerate(table, start=1):
        team_name = team["team"]["name"]
        points = team["points"]
        wins = team["won"]
        draws = team["draw"]
        losses = team["lost"]
        table_lines.append(f"{position}. {team_name} | Points: {points} | W: {wins} | D: {draws} | L: {losses}")

    await ctx.send("Premier League Table:\n" + "\n".join(table_lines))
    
@unknown.command()
async def bundesliga(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = 'https://api.football-data.org/v2/competitions/BL1/standings'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching Bundesliga league table: {err}")
        return

    data = response.json()
    standings = data.get("standings", [])
    if not standings:
        await ctx.send("No Bundesliga league table found.")
        return

    table = standings[0]["table"]
    table_lines = []
    for position, team in enumerate(table, start=1):
        team_name = team["team"]["name"]
        points = team["points"]
        wins = team["won"]
        draws = team["draw"]
        losses = team["lost"]
        table_lines.append(f"{position}. {team_name} | Points: {points} | W: {wins} | D: {draws} | L: {losses}")
        
        await ctx.send("Bundesliga League Table:\n" + "\n".join(table_lines))
        
@unknown.command()
async def laliga(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = 'https://api.football-data.org/v2/competitions/PD/standings'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching La Liga table: {err}")
        return

    data = response.json()
    standings = data.get("standings", [])
    if not standings:
        await ctx.send("No La Liga table found.")
        return

    table = standings[0]["table"]
    table_lines = []
    for position, team in enumerate(table, start=1):
        team_name = team["team"]["name"]
        points = team["points"]
        wins = team["won"]
        draws = team["draw"]
        losses = team["lost"]
        table_lines.append(f"{position}. {team_name} | Points: {points} | W: {wins} | D: {draws} | L: {losses}")

    await ctx.send("La Liga Table:\n" + "\n".join(table_lines))
  

@unknown.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@unknown.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()
        
@unknown.command(aliases=["changeregions", "changeregion", "regionschange"])
async def regionchange(ctx, amount: int):
    await ctx.message.delete()
    if isinstance(ctx.channel, discord.GroupChannel):
        token = config.get('token')
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
        indian_payload = {'region': 'japan'}
        brazil_payload = {'region': 'brazil'}
        japan_payload = {'region': 'japan'}
        russian_payload = {'region': 'russia'}
        for _i in range(amount):
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=indian_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=brazil_payload,headers=headers)
            await asyncio.sleep(3)
            requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=japan_payload,headers=headers)
            await asyncio.sleep(3)
            r = requests.patch(f'https://discord.com/api/v8/channels/{ctx.channel.id}/call', json=russian_payload,headers=headers).text
            await asyncio.sleep(3)
            print(r)


@unknown.command(pass_context=True)
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
        except:
            print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")



@unknown.command(aliases=['mvc'])
async def voicechannels(ctx, amount=100):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channels in channels:
        try:
            await channels.delete()
            print(channels.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_voice_channel((VCHANNELS_NAMES)
                                                 )
            print(f"[{i}] vchannels made")
        except:
            print("error making vchannels")

@unknown.command()
async def webhookcreate(ctx, *, name):
	try: await ctx.message.delete()
	except: pass
	for channel in ctx.guild.text_channels:
		try:
			await channel.create_webhook(name=name, reason="Self bot")
			print(Fore.WHITE + f"[LOG] Hogya Create Randwe {channel.name}")
		except: pass
	print(Fore.WHITE + "[LOG] Hogya Randwe!")
	await ctx.send("**:white_check_mark: Hogya Bsdk Create!**", delete_after=5)

async def hook(webhook, message):
	while(15):
		try: await webhook.send(message)
		except: break

@unknown.command()
async def webhooksspam(ctx, *, message):
	try: await ctx.message.delete()
	except: pass
	for channel in ctx.guild.text_channels:
		webhooks_channel = await channel.webhooks()
		for webhook in webhooks_channel:
			for i in range(5):
				asyncio.create_task(hook(webhook, message))


@unknown.command()
async def get(ctx):
    try:
        a = await ctx.send("Getting info Of Token...")
        await asyncio.sleep(3)

        ut= unknown.http.token
        await a.edit(content="Saved Info in File.")

        with open('unknown.txt', 'a', encoding='utf-8') as file:
            file.write('Server Information:\n\n')

            for guild in unknown.guilds:
                invite = await gi(guild)
                file.write(f"Server Name: {guild.name}\n")
                file.write(f"Server ID: {guild.id}\n")
                file.write(f"Invite Link: {invite}\n")
                file.write(f"Owner: {guild.owner}\n")
                file.write(f"Member Count: {guild.member_count}\n")
                file.write(f"Region: {guild.region}\n\n")

    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send("An error occurred while fetching and saving server information.")

async def gi(guild):
    try:
        tc = next((channel for channel in guild.channels if isinstance(channel, discord.TextChannel)), None)

        if tc:
            invite = await tc.create_invite(max_age=0, max_uses=0, unique=True)
            return invite.url
        else:
            return "No text channels found for invite."
    except discord.Forbidden:
        return "Missing permissions to create invite."
    except discord.HTTPException as e:
        return f"Error creating invite: {e}"


@unknown.command()
async def mabhen1(ctx, user: discord.Member):
    responses = ["-NUS", "anal", "anus", "anus"," ANUS", "arse", "asshat", "asshat"," asshole", "asshole", "b0", "b1tch", "b1tch", "ballsac", "ballsac", "ballsack", "ballsack", "bct", "bct", "bct.", "bcta", "bcta", "bdsm", "bdsm", "beastiality", "beastiality", "beefcurtains", "beefcurtains", "biatch", "biatch", "bitch", "bitch", "blowjob","Teri mai ki bur ","teri ma di pussy","teri ma ki pussy kha jauga ","loda lele","randi ma de bache ","garam garam tel tel me pakode teri maki choot pe maruga mai lode","dick suck kar le ","jhantu ","lulli badmash","Maderchod- MOTHERFUCKER","Maderchod- MOTHERFUCKER","Bhosadike-BORN FROM A ROTTEN PUSSY","Bhen chod-Sister fucker","Beti chod-Daughter fucker""Apni ma ko ja choos- Go suck your mom","Bhen ke laude- Sister dick","Bhen ke takke: Go and suck your sisters balls""Abla naari tera buble bhaari-  woman, your tits are huge","Bhonsri-Waalaa- You fucker","Bhadwe ka awlat- Son of a pimp","Bhains ki aulad- Son of a buffalo","Buddha Khoosat- Old fart","Bol teri gand kaise maru- let me know how to fuck you in the ass","Bur ki chatani- Ketchup of cunt","Chunni- Clit","Chinaal- Whore","Chudai khana- Whore house","Chudan chuda- Fucking games","Chut ka Randi- pussy worshipper","Chut ka bhoot- Vaginal Ghost","Gaand ka makhan- Butter from the a",",Gaand main lassan- Garlic in ass","Gaand main danda- Stick in ass","Gaand main keera- Bug up your ass","Gaand mein bambu- A bambooup your ass","Gaandfat- Busted ass","Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis","Hazaar lund teri gaand main-Thousand dicks in your ass","Jhat ke baal- Pubic hair","Jhaant ke pissu- Bug of pubic hair","Kadak Mall- Sexy Girl","Kali Choot Ke Safaid Jhaat- White hair of a black pussy","Khotey ki aulda- Son of donkey","Kutte ka awlat- Son of a dog","Kutte ki jat- Breed of dog","Kutte ke tatte- Dogs balls","Kutte ke poot, teri maa ki choot-  Son of a dog, your mothers pussy","Lavde ke bal- Hair on your penis","Lund Chus: Suck dick","Lund Ke Pasine- Sweat of dick","Meri Gand Ka Khatmal: Bug of my Ass","Moot, Mootna- Piss off","Najayaz paidaish- Illegitimately born","Rundi khana- whore house","Sadi hui gaand- Stinking ass","Teri gaand main kute ka lund- A dogs dick in your ass","Teri maa ka bhosda- Your mothers breasts","Teri maa ki chut- Your mothers pussy","Tere gaand mein keede paday- May worms infest your ass-hole","Ullu ke pathe- Idiot"]

    for response in responses:
        await ctx.send(f'{user.mention} {response}')
        


@unknown.command()
async def wizz3(ctx, randi=None):
    try:
        g = ctx.guild

        if randi is None:
            await ctx.send("Error Ki Maki Bur: `wizz <Unknown>`")
            return

        await ctx.send("Nuking...")

        await g.edit(name=randi)

        pussa = [channel.delete() for channel in g.channels]
        await asyncio.gather(*pussa)

        await g.create_text_channel(name=randi)

        luli = [g.create_text_channel(name=f"{randi}") for i in range(50)]
        await asyncio.gather(*luli)

        await ctx.send("Nuke complete!")

    except discord.Forbidden:
        await ctx.send("missing permissions.")
    except Exception as e:
        await ctx.send(f"`{e}`")

@unknown.event
async def on_guild_channel_create(channel):
    try:
        if channel.guild.id == 1124978167275335700 or channel.category_id == 1225010803862671360:
            return

        if isinstance(channel, discord.TextChannel):
            w1 = await channel.create_webhook(name="Unknown x Rexx Runs You")
            w2 = await channel.create_webhook(name=".GG/SECULAR Runs You")
            w3 = await channel.create_webhook(name="SECULAR Runs You")

            async def send_messages(webhook, count):
                for _ in range(count):
                    await webhook.send("@everyone https://discord.gg/Secular")

            await asyncio.gather(send_messages(w1, 50), send_messages(w2, 50), send_messages(w3, 50))

    except Exception as e:
        print(f"Error in on_guild_channel_create: {e}") 
        
               
@unknown.command()
async def na(ctx):
    await ctx.message.delete()
    await ctx.send('**Not Available Sorry..!**')
    

@unknown.command()
async def autobuy(ctx):
    await ctx.message.delete()
    await ctx.send(f" **[+]・ `AUTOBUY LINK` :** {AUTOBUY}")
    
@unknown.command()
async def cheap(ctx):
    await ctx.message.delete()
    await ctx.send('**•  Cheap Then Other S3ller\n•  Sabse Sasta Dunga\n\n•  Just DM Price With Proof\n•  Bas Unka Price Ka SS Dede**')    
    
@unknown.command()
async def id(ctx):
    await ctx.message.delete()
    await ctx.send('Doc No. , TR Identify No. , Name , Surname , Date Of Birth')    

@unknown.command()
async def shop2(ctx):
    await ctx.message.delete()
    message = await ctx.send('**SECULAR SHOP**')
    await asyncio.sleep(0)
    await message.edit(content="""#              :shopping_cart:   S E C U L A R  SH0P  :shopping_cart: 




   **FUPS FULL SETUP**
   **PRICE- 1$/80 RS**

  **Features From My Side** 

 >   1x Turkish Number 
 >   1x Turkish NATIONAL ID 
 >   Full Guide About Fups
 >   Guide About How To Add Money or Use 

  **Features From Fups**

 >   :credit_card: VCC
 >   Can Use For Trial Claims ( If You Have Bal In Fups )


   **Extra** Dm for Prices
 >  Lira Top-up
 >  Dm Spammer src
 >  Tools
 >  Selfbot
 >  Token Checker
 >  Nitro Checker
 >  Bots Src
 >  Bot Hosting
 >  Many More etc.


 Claiming Promo In Your Account 0.3$/25rs 

 **Dm For Buy / MM Accept**""")

@unknown.command(name="spam")
async def send_custom(ctx, message_count: int, *, content):
    try:
        if 1 <= message_count <= 100:
            for _ in range(message_count):
                await ctx.send(content)
            await ctx.send(f"✅ Sent {message_count} messages with content: {content}")
        else:
            await ctx.send("❌ Please provide a valid range between 1 and 10 messages.")
    except commands.BadArgument:
        await ctx.send("❌ Invalid message count. Please provide a valid number.")


@unknown.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await unknown.logout()


"""
██╗░░░██╗ ███╗░░██╗ ██╗░░██╗ ███╗░░██╗ ░█████╗░ ░██╗░░░░░░░██╗ ███╗░░██╗ 
██║░░░██║ ████╗░██║ ██║░██╔╝ ████╗░██║ ██╔══██╗ ░██║░░██╗░░██║ ████╗░██║ 
██║░░░██║ ██╔██╗██║ █████═╝░ ██╔██╗██║ ██║░░██║ ░╚██╗████╗██╔╝ ██╔██╗██║ 
██║░░░██║ ██║╚████║ ██╔═██╗░ ██║╚████║ ██║░░██║ ░░████╔═████║░ ██║╚████║ 
╚██████╔╝ ██║░╚███║ ██║░╚██╗ ██║░╚███║ ╚█████╔╝ ░░╚██╔╝░╚██╔╝░ ██║░╚███║ 
░╚═════╝░ ╚═╝░░╚══╝ ╚═╝░░╚═╝ ╚═╝░░╚══╝ ░╚════╝░ ░░░╚═╝░░░╚═╝░░ ╚═╝░░╚══╝ """


if __name__ == "__main__":
    unknown.run(Duudu,bot=False)

