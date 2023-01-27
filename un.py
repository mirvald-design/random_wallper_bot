import requests
import json
import time
from telegram import Bot

# Telegram Bot Token
TOKEN = '5911723724:AAGPiMd-3hlewv-d-TsX5UUOxTVN-koKu0A'

# Unsplash API Key
UNSPLASH_API_KEY = 'tfvxxDiG8qhrVGT6uQpMa1T73Py7mNJuKNeUVX95PxY'

# Telegram Channel ID
CHANNEL_ID = '-1001724715196'

# Interval in seconds
INTERVAL = 30

bot = Bot(TOKEN)

while True:
    # Get a random photo from Unsplash
    r = requests.get(f'https://api.unsplash.com/photos/random?client_id={UNSPLASH_API_KEY}&orientation=portrait')
    data = json.loads(r.text)
    photo_url = data['urls']['full']

    # Send the photo to the Telegram channel
    bot.send_photo(chat_id=CHANNEL_ID, photo=photo_url)

    # Wait for the specified interval
    time.sleep(INTERVAL)
