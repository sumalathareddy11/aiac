import csv

input_file = 'iot_sensor_drift_corrected.csv'
output_file = 'iot_sensor_normalized.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)

# Extract temperature and humidity as floats, handle missing/invalid values
temperature_vals = []
humidity_vals = []
for row in rows:
    try:
        temp = float(row.get('temperature', '').strip())
    except (ValueError, TypeError):
        temp = None
    temperature_vals.append(temp)
    try:
        hum = float(row.get('humidity', '').strip())
    except (ValueError, TypeError):
        hum = None
    humidity_vals.append(hum)

# Compute mean and std for standard scaling (ignoring None)
def mean_std(values):
    valid = [v for v in values if v is not None]
    if not valid:
        return 0.0, 1.0
    mean = sum(valid) / len(valid)
    std = (sum((v - mean) ** 2 for v in valid) / len(valid)) ** 0.5
    if std == 0:
        std = 1.0
    return mean, std

temp_mean, temp_std = mean_std(temperature_vals)
hum_mean, hum_std = mean_std(humidity_vals)

# Normalize and update rows
for i, row in enumerate(rows):
    temp = temperature_vals[i]
    hum = humidity_vals[i]
    if temp is not None:
        norm_temp = (temp - temp_mean) / temp_std
        row['temperature'] = f"{norm_temp:.6f}"
    else:
        row['temperature'] = ''
    if hum is not None:
        norm_hum = (hum - hum_mean) / hum_std
        row['humidity'] = f"{norm_hum:.6f}"
    else:
        row['humidity'] = ''

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the normalized results
for row in rows:
    print(row)
