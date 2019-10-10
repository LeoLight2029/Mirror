import discord
from discord import Webhook, AsyncWebhookAdapter
from discord import ext
from discord.ext import commands
import asyncio
import sys
import requests
import aiohttp
import io
import gc

client = discord.Client()
token = "Ur token here"
blacklistedwebhook = ["idofwebhook1", "idofwebhook2"]

fromchannel = int(sys.argv[1])
webtoken = sys.argv[2]

@client.event
async def on_ready():
    print ("Logged in")
    

@client.event
async def on_message(message):
    gc.collect()
    fchannel = client.get_channel(fromchannel)
    if message.channel == fchannel and message.webhook_id not in blacklistedwebhook:
        attach = message.attachments
        sentembed = message.embeds
        print ("Forwarding this message: "+ message.content)
        if attach:
            for attachment in attach:
                print (attachment)
                fp = io.BytesIO()
                await attachment.save(fp)
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(webtoken, adapter=AsyncWebhookAdapter(session))
                    await webhook.send(content=message.clean_content, username=message.author.display_name, avatar_url=message.author.avatar_url, file=discord.File(fp, filename=attachment.filename))
        else:
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webtoken, adapter=AsyncWebhookAdapter(session))
                await webhook.send(content=message.clean_content, username=message.author.display_name, avatar_url=message.author.avatar_url)

client.run(token, bot=False)
