import discord
import asyncio
import subprocess
import sys

import os






print("██████╗  █████╗      ██╗ █████╗     ██████╗ ██╗      █████╗ ███████╗████████╗")
print("██╔══██╗██╔══██╗     ██║██╔══██╗    ██╔══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝")
print("██████╔╝███████║     ██║███████║    ██████╔╝██║     ███████║███████╗   ██║   ")
print("██╔══██╗██╔══██║██   ██║██╔══██║    ██╔══██╗██║     ██╔══██║╚════██║   ██║   ")
print("██████╔╝██║  ██║╚█████╔╝██║  ██║    ██████╔╝███████╗██║  ██║███████║   ██║   ")
print("╚═════╝ ╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ")
                                                                             





def set_terminal_title(title):
    if os.name == 'nt':  # For Windows
        os.system(f'title {title}')
    elif os.name == 'posix':  # For Linux/MacOS
        print(f'\033]0;{title}\007', end='', flush=True)


set_terminal_title("Baja Blast SelfBot`")


client = discord.Client()

async def send_link():
    link = "REPLACE ME WITH UR SPAM TEXT "
    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send(link)
                print(f"Spam sent in {guild.name}")
            except discord.errors.Forbidden:
                print(f"Missing permissions in {guild.name}")
            except discord.errors.HTTPException as e:
                print(f"Error")

async def reopen():
    await asyncio.sleep(60)  # Wait for a minute before reopening
    subprocess.Popen([sys.executable] + sys.argv)  # Reopen the script

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await send_link()
    await reopen()


client.run('Replace with ur token', bot=False)