import re
import emoji
import pandas as pd

def preprocess_text(text):
    if not text or not isinstance(text, str):
        return ""
    text = emoji.replace_emoji(text, replace="")
    text = re.sub(r'\s+', ' ', text.strip())
    text = re.sub(r'[\.\-\_\+\=\*]+', ' ', text)
    price_match = re.search(r'(\d+\s?ብር)', text)
    price = price_match.group(0) if price_match else ""
    tokens = text.split()
    cleaned_text = ' '.join(token for token in tokens if token not in ['💥', '🔥', '👍', '📌', '🏢', '📍', '💧', '📲', '🔖', '💬'])
    return f"{cleaned_text} [Price: {price}]" if price else cleaned_text

# Read CSV
input_file = 'telegram_data.csv'
output_file = 'preprocessed_telegram_data.csv'

df = pd.read_csv(input_file)
df['text'] = df['text'].apply(preprocess_text)

# Save preprocessed data
df.to_csv(output_file, index=False, encoding='utf-8')
print("Preprocessing complete. Saved to preprocessed_telegram_data.csv")