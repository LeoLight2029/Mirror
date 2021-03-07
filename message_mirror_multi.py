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
blacklistedwebhook = ["idofwebhook1", "idofwebhook2"] #put all of the webhooks here
channelsdict = {
channel_id: "webhook url",
} #Just put all the channels to mirror and where they will be mirrored in this dict

@client.event
async def on_ready():
    print ("Logged in")    

@client.event
async def on_message(message):
    if message.channel.id in channelsdict.keys():
        if message.webhook_id == None or message.webhook_id not in blacklistedwebhook:
            attach = message.attachments
            sentembed = message.embeds
            print ("Forwarding this message: "+ message.content)
            #print(message.webhook_id)
            if attach:
                for attachment in attach:
                    print (attachment)
                    fp = io.BytesIO()
                    await attachment.save(fp)
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(channelsdict[message.channel.id], adapter=AsyncWebhookAdapter(session))
                        await webhook.send(content=message.clean_content, username=message.author.display_name, avatar_url=message.author.avatar_url, file=discord.File(fp, filename=attachment.filename), embeds=sentembed)
            else:
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(channelsdict[message.channel.id], adapter=AsyncWebhookAdapter(session))
                    await webhook.send(content=message.clean_content, username=message.author.display_name, avatar_url=message.author.avatar_url, embeds=sentembed)

client.run(token, bot=False)
