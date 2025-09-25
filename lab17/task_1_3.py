import csv
from datetime import datetime

input_file = 'social_media_cleaned_filled.csv'
output_file = 'social_media_final.csv'

with open(input_file, 'r', encoding='utf-8', newline='') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames.copy()
    # Add new feature columns if not already present
    if 'hour' not in fieldnames:
        fieldnames.append('hour')
    if 'weekday' not in fieldnames:
        fieldnames.append('weekday')
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    final_rows = []
    for row in reader:
        timestamp = row.get('timestamp', '')
        hour = ''
        weekday = ''
        if timestamp:
            try:
                # Try parsing common timestamp formats
                # Example: '2023-06-01 14:23:45'
                dt = None
                for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%d"):
                    try:
                        dt = datetime.strptime(timestamp, fmt)
                        break
                    except ValueError:
                        continue
                if dt:
                    hour = str(dt.hour)
                    weekday = str(dt.weekday())  # Monday=0, Sunday=6
            except Exception:
                pass
        row['hour'] = hour
        row['weekday'] = weekday
        writer.writerow(row)
        final_rows.append(row)

# Print the final results
for row in final_rows:
    print(row)
