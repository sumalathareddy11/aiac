import csv
import string

# Define a basic set of English stopwords
STOPWORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could',
    "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for',
    'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's",
    'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm",
    "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't",
    'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours',
    'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so',
    'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there',
    "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too',
    'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what',
    "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with',
    "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself',
    'yourselves'
}

def clean_text(text):
    # Remove punctuation and special symbols
    text = text.lower()
    text = ''.join(ch if ch.isalnum() or ch.isspace() else ' ' for ch in text)
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]
    return ' '.join(words)

input_file = 'social_media.csv'
output_file = 'social_media_cleaned.csv'

with open(input_file, 'r', encoding='utf-8', newline='') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    # Find the post text column (try common names)
    post_col = None
    for candidate in ['post', 'text', 'content', 'message']:
        if candidate in fieldnames:
            post_col = candidate
            break
    if not post_col:
        post_col = fieldnames[0]  # fallback to first column

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    cleaned_rows = []
    for row in reader:
        original = row[post_col]
        row[post_col] = clean_text(original)
        writer.writerow(row)
        cleaned_rows.append(row)

# Print the cleaned results
for row in cleaned_rows:
    print(row)
