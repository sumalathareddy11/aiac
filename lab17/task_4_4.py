import csv

input_file = 'movie_reviews_filled.csv'
output_file = 'movie_reviews_normalized.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# Normalize ratings (0–10 → 0–1 scale)
for row in rows:
    rating_str = row.get('rating', '').strip()
    try:
        rating = float(rating_str)
        normalized = rating / 10.0
        row['rating_normalized'] = f"{normalized:.3f}"
    except (ValueError, TypeError):
        row['rating_normalized'] = ""

# Add new field if not present
if 'rating_normalized' not in fieldnames:
    fieldnames.append('rating_normalized')

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the normalized results
for row in rows:
    print(row)
