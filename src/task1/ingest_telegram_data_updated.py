from telethon.sync import TelegramClient
from telethon.tl.types import Channel
import csv
import re
import emoji
from nltk.tokenize import word_tokenize

# Replace with your own API credentials
api_id = '20656473'
api_hash = 'acb15e8b83308ccc2167fffc159b750d'
phone = '+251941226023'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

def preprocess_text(text):
    if not text or not isinstance(text, str):
        return ""
    text = emoji.replace_emoji(text, replace="")
    text = re.sub(r'\s+', ' ', text.strip())
    text = re.sub(r'[\.\-\_\+\=\*]+', ' ', text)
    price_match = re.search(r'(\d+\s?ብር)', text)
    price = price_match.group(0) if price_match else ""
    tokens = word_tokenize(text)
    cleaned_text = ' '.join(token for token in tokens if token not in ['💥', '🔥', '👍', '📌', '🏢', '📍', '💧', '📲', '🔖', '💬'])
    return f"{cleaned_text} [Price: {price}]" if price else cleaned_text

async def main():
    await client.start(phone)
    channels = ['@ZemenExpress', '@nevacomputer', '@meneshayeofficial', '@ethio_brand_collection', '@Leyueqa']
    all_messages = []

    for channel in channels:
        entity = await client.get_entity(channel)
        async for message in client.iter_messages(entity, limit=100):
            text = preprocess_text(message.message) if message.message else ""
            all_messages.append({
                'channel': channel,
                'text': text,
                'timestamp': message.date.isoformat(),
                'views': getattr(message, 'views', 0)
            })

    # Save to CSV
    with open('preprocessed_telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['channel', 'text', 'timestamp', 'views'])
        writer.writeheader()
        writer.writerows(all_messages)

with client:
    client.loop.run_until_complete(main())