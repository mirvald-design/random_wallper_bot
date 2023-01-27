import requests
import json
import asyncio
import time
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("PEXELS_API_KEY")
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
channel_id = os.environ.get("TELEGRAM_CHANNEL_ID")


async def fetch_photos():
    url = f'https://api.pexels.com/v1/curated?per_page=1&page=1'
    headers = {'Authorization': api_key}
    try:
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        photo_url = data['photos'][0]['src']['original']
        photo_photographer = data['photos'][0]['photographer']
    finally:
        response.close()
    return photo_url, photo_photographer


async def send_photo_to_telegram(photo_url, photo_photographer):
    bot = Bot(token=bot_token)
    try:
        await bot.send_photo(chat_id=channel_id, photo=photo_url, caption=photo_photographer)
    except Exception as e:
        print("An error occurred: ", e)


async def main():
    while True:
        photo_url, photo_photographer = await fetch_photos()
        await send_photo_to_telegram(photo_url, photo_photographer)
        time.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())

