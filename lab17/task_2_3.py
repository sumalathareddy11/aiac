import csv
import math

input_file = 'financial_data_updated.csv'  # output of task_2_2.py
output_file = 'financial_data_logvol.csv'

rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    if 'log_volume' not in fieldnames:
        fieldnames = fieldnames + ['log_volume']
    for row in reader:
        # Normalize volume using log-scaling
        try:
            volume = float(row.get('volume', 0))
            # To avoid log(0), add 1
            log_volume = math.log(volume + 1)
        except (ValueError, TypeError):
            log_volume = 0.0
        row['log_volume'] = f"{log_volume:.6f}"
        rows.append(row)

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Print the updated results
for row in rows:
    print(row)
