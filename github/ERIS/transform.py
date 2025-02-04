from transformers import BertTokenizer

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def preprocess_text(text):
    """Tokenizes and encodes text for BERT model."""
    tokens = tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")
    return tokens

# Example news headline for processing
sample_text = "Company stock may fall due to regulatory issues."
processed_text = preprocess_text(sample_text)

print("✅ News article successfully tokenized for BERT model.")
