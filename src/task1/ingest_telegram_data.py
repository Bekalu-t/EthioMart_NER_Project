from telethon.sync import TelegramClient
from telethon.tl.types import Channel
import csv

# Replace with your own API credentials
api_id = '20656473'
api_hash = 'acb15e8b83308ccc2167fffc159b750d'
phone = '+251941226023'

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)
    channels = ['@ZemenExpress', '@nevacomputer', '@meneshayeofficial', '@ethio_brand_collection', '@Leyueqa']
    all_messages = []

    for channel in channels:
        entity = await client.get_entity(channel)
        async for message in client.iter_messages(entity, limit=100):  # Fetch last 100 messages
            all_messages.append({
                'channel': channel,
                'text': message.message,
                'timestamp': message.date.isoformat(),
                'views': getattr(message, 'views', 0)
            })

    # Save to CSV
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['channel', 'text', 'timestamp', 'views'])
        writer.writeheader()
        writer.writerows(all_messages)

with client:
    client.loop.run_until_complete(main())