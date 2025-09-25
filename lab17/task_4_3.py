import csv

input_file = 'movie_reviews_tfidf.csv'
output_file = 'movie_reviews_filled.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# Collect all non-missing ratings
ratings = []
for row in rows:
    rating_str = row.get('rating', '').strip()
    try:
        rating = float(rating_str)
        ratings.append(rating)
    except (ValueError, TypeError):
        continue

# Compute median
if ratings:
    sorted_ratings = sorted(ratings)
    n = len(sorted_ratings)
    if n % 2 == 1:
        median_rating = sorted_ratings[n // 2]
    else:
        median_rating = (sorted_ratings[n // 2 - 1] + sorted_ratings[n // 2]) / 2
else:
    median_rating = 0.0  # fallback if no ratings

# Fill missing ratings with median
for row in rows:
    rating_str = row.get('rating', '').strip()
    try:
        float(rating_str)
    except (ValueError, TypeError):
        row['rating'] = f"{median_rating:.1f}"

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the filled results
for row in rows:
    print(row)
