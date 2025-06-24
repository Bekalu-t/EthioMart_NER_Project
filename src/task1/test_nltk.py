import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Test with English
text = "This is a test."
tokens = word_tokenize(text, language='english')
print(tokens)

# Fallback for Amharic with simple split
amharic_text = "ዋጋ፦ 700 ብር"
tokens_am = amharic_text.split()
print(tokens_am)