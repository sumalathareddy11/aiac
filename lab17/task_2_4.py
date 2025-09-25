import csv
input_file = 'financial_data.csv'
output_file = 'financial_data_no_outliers.csv'
closing_prices = []
rows = []
with open(input_file, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    for row in reader:
        try:
            price = float(row['closing_price'])
        except (ValueError, TypeError):
            price = 0.0
        closing_prices.append(price)
        row['closing_price'] = price
        rows.append(row)
sorted_prices = sorted(closing_prices)
n = len(sorted_prices)
def percentile(data, percent):
    k = (len(data)-1) * percent
    f = int(k)
    c = min(f+1, len(data)-1)
    if f == c:
        return data[int(k)]
    d0 = data[f] * (c-k)
    d1 = data[c] * (k-f)
    return d0 + d1
Q1 = percentile(sorted_prices, 0.25)
Q3 = percentile(sorted_prices, 0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
filtered_rows = []
for row in rows:
    price = row['closing_price']
    if lower_bound <= price <= upper_bound:
        filtered_rows.append(row)
for row in filtered_rows:
    row['closing_price'] = f"{row['closing_price']}"
with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)
for row in filtered_rows:
    print(row)
