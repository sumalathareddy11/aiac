import csv
import re

input_file = 'movie_reviews-1.csv'
output_file = 'movie_reviews_cleaned.csv'

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Convert to lowercase
    return text.lower()

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        # Assume the review text is in a column named 'review'
        if 'review' in row:
            row['review'] = clean_text(row['review'])
        rows.append(row)

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the cleaned results
for row in rows:
    print(row)

