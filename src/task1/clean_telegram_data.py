import csv
import pandas as pd

def clean_and_structure_data(input_file, output_file):
    # Read CSV
    df = pd.read_csv(input_file)
    
    # Remove rows with empty text
    df = df[df['text'].notna() & (df['text'] != '')]
    
    # Deduplicate based on timestamp and text
    df = df.drop_duplicates(subset=['timestamp', 'text'], keep='first')
    
    # Save cleaned data
    df.to_csv(output_file, index=False, encoding='utf-8')

# Example usage
clean_and_structure_data('telegram_data.csv', 'cleaned_telegram_data.csv')