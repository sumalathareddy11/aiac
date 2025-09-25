import csv

input_file = 'iot_sensor_updated.csv'
output_file = 'iot_sensor_drift_corrected.csv'

window_size = 3

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)
def rolling_mean(values, window):
    result = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        window_vals = values[start:i+1]
        # Only use valid floats
        window_vals = [v for v in window_vals if v is not None]
        if window_vals:
            result.append(sum(window_vals) / len(window_vals))
        else:
            result.append(None)
    return result

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

temperature_smoothed = rolling_mean(temperature_vals, window_size)
humidity_smoothed = rolling_mean(humidity_vals, window_size)

# Update rows with drift-corrected values
for i, row in enumerate(rows):
    if temperature_smoothed[i] is not None:
        row['temperature'] = f"{temperature_smoothed[i]:.2f}"
    else:
        row['temperature'] = ''
    if humidity_smoothed[i] is not None:
        row['humidity'] = f"{humidity_smoothed[i]:.2f}"
    else:
        row['humidity'] = ''

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the drift-corrected results
for row in rows:
    print(row)
    
