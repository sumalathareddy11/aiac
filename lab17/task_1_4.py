import csv

input_file = 'social_media_final.csv'
output_file = 'social_media_nospam.csv'

seen_posts = set()
unique_rows = []

with open(input_file, 'r', encoding='utf-8', newline='') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        # Use post_text as the main indicator for duplicates/spam
        post_text = row.get('post_text', '').strip().lower()
        # Optionally, you can use a tuple of (post_text, user) for more strictness
        key = post_text
        if key not in seen_posts and post_text != '':
            seen_posts.add(key)
            writer.writerow(row)
            unique_rows.append(row)

# Print the deduplicated results
for row in unique_rows:
    print(row)
