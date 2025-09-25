import csv

input_file = 'social_media_cleaned.csv'
output_file = 'social_media_cleaned_filled.csv'

with open(input_file, 'r', encoding='utf-8', newline='') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    updated_rows = []
    for row in reader:
        # Handle missing values in 'likes' and 'shares'
        for col in ['likes', 'shares']:
            if col in row:
                value = row[col]
                if value is None or value.strip() == '':
                    row[col] = '0'
        writer.writerow(row)
        updated_rows.append(row)

# Print the updated results
for row in updated_rows:
    print(row)
