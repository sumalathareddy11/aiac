import csv

input_file = 'iot_sensor.csv'
output_file = 'iot_sensor_updated.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# Forward fill missing values for each column
last_valid = {}
for row in rows:
    for field in fieldnames:
        value = row.get(field, '').strip()
        if value == '' or value.lower() == 'na':
            # Use last valid value if available, else keep as empty
            row[field] = last_valid.get(field, '')
        else:
            last_valid[field] = value

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the cleaned results
for row in rows:
    print(row)
