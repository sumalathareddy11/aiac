import csv

input_file = 'financial_data.csv'
output_file = 'financial_data_updated.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        # Handle missing values for closing_price
        closing_price = row.get('closing_price', '').strip()
        if closing_price == '' or closing_price.lower() == 'na':
            row['closing_price'] = '0'
        # Handle missing values for volume
        volume = row.get('volume', '').strip()
        if volume == '' or volume.lower() == 'na':
            row['volume'] = '0'
        rows.append(row)

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the updated results
for row in rows:
    print(row)
