import csv
import math
from collections import Counter, defaultdict

input_file = 'movie_reviews_cleaned.csv'
output_file = 'movie_reviews_tfidf.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

review_texts = [row['review'] for row in rows if 'review' in row]
tokenized_reviews = [text.split() for text in review_texts]

# Build vocabulary
vocab = sorted(set(word for tokens in tokenized_reviews for word in tokens))
df = defaultdict(int)
for tokens in tokenized_reviews:
    unique_tokens = set(tokens)
    for token in unique_tokens:
        df[token] += 1

N = len(tokenized_reviews)
# Compute IDF for each term
idf = {}
for term in vocab:
    # Add 1 to denominator for smoothing
    idf[term] = math.log((N + 1) / (df[term] + 1)) + 1

# Prepare new fieldnames for output
tfidf_fieldnames = list(fieldnames) + [f"tfidf_{feat}" for feat in vocab]

# Add TF-IDF features to each row
for i, row in enumerate(rows):
    if i < len(tokenized_reviews):
        tokens = tokenized_reviews[i]
        tf = Counter(tokens)
        length = len(tokens)
        for term in vocab:
            tf_val = tf[term] / length if length > 0 else 0.0
            tfidf_val = tf_val * idf[term]
            row[f"tfidf_{term}"] = f"{tfidf_val:.6f}"
    else:
        for term in vocab:
            row[f"tfidf_{term}"] = ""

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=tfidf_fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the encoded results
for row in rows:
    print(row)
