import csv

input_file = 'financial_data_updated.csv'
output_file = 'financial_data_with_lags.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['return_1d', 'return_7d']
    for row in reader:
        # Convert closing_price to float for calculations
        try:
            row['closing_price'] = float(row['closing_price'])
        except (ValueError, TypeError):
            row['closing_price'] = 0.0
        rows.append(row)

# Sort rows by date ascending (assuming 'date' column exists)
rows.sort(key=lambda x: x['date'])

# Calculate lag features
for i, row in enumerate(rows):
    # 1-day return
    if i > 0:
        prev_close = rows[i-1]['closing_price']
        if prev_close != 0:
            row['return_1d'] = (row['closing_price'] - prev_close) / prev_close
        else:
            row['return_1d'] = 0.0
    else:
        row['return_1d'] = 0.0

    # 7-day return
    if i >= 7:
        prev7_close = rows[i-7]['closing_price']
        if prev7_close != 0:
            row['return_7d'] = (row['closing_price'] - prev7_close) / prev7_close
        else:
            row['return_7d'] = 0.0
    else:
        row['return_7d'] = 0.0

# Convert return values to string for CSV output
for row in rows:
    row['return_1d'] = f"{row['return_1d']:.6f}"
    row['return_7d'] = f"{row['return_7d']:.6f}"
    # Optionally, convert closing_price back to string
    row['closing_price'] = f"{row['closing_price']}"

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the updated results
for row in rows:
    print(row)
