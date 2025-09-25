import csv

input_file = 'iot_sensor_drift_corrected.csv'
output_file = 'iot_sensor_encoded.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames.copy()
    if 'sensor_id' not in fieldnames:
        raise ValueError("Expected 'sensor_id' column in input file.")
    for row in reader:
        rows.append(row)

# Encode categorical sensor IDs
sensor_ids = sorted({row['sensor_id'] for row in rows if row['sensor_id'] != ''})
sensor_id_to_int = {sid: idx for idx, sid in enumerate(sensor_ids)}
# Add new column for encoded sensor id
encoded_field = 'sensor_id_encoded'
if encoded_field not in fieldnames:
    fieldnames.append(encoded_field)

for row in rows:
    sid = row.get('sensor_id', '')
    if sid in sensor_id_to_int:
        row[encoded_field] = str(sensor_id_to_int[sid])
    else:
        row[encoded_field] = ''

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the encoded results
for row in rows:
    print(row)
