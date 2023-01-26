import requests
import json
import time
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PEXELS_API_KEY")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
channel_id = os.getenv("TELEGRAM_CHANNEL_ID")


def fetch_photos():
    url = f'https://api.pexels.com/v1/curated?per_page=1&page=1'
    headers = {'Authorization': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    photo_url = data['photos'][0]['src']['original']
    photo_photographer = data['photos'][0]['photographer']
    return photo_url, photo_photographer


def send_photo_to_telegram(photo_url, photo_photographer):
    bot = Bot(token=bot_token)
    bot.send_photo(chat_id=channel_id, photo=photo_url, caption=photo_photographer)


while True:
    photo_url, photo_photographer = fetch_photos()
    send_photo_to_telegram(photo_url, photo_photographer)
    time.sleep(10) # wait for 1 hour before fetching and sending another photo
