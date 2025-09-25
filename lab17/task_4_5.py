import csv

def print_summary(title, rows, fieldnames, num_rows=5):
    print(f"\n{'='*40}\n{title}\n{'='*40}")
    print(f"Total rows: {len(rows)}")
    print(f"Fields: {fieldnames}")
    print("Sample rows:")
    for row in rows[:num_rows]:
        print(row)
    if len(rows) > num_rows:
        print("...")

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    return rows, fieldnames

# File names for before and after
before_file = 'movie_reviews_filled.csv'
after_file = 'movie_reviews_normalized.csv'

# Load data
before_rows, before_fields = load_csv(before_file)
after_rows, after_fields = load_csv(after_file)

# Print summary report
print_summary("Before (movie_reviews_filled.csv)", before_rows, before_fields)
print_summary("After (movie_reviews_normalized.csv)", after_rows, after_fields)
