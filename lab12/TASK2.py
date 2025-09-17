import time
import csv
# Function to load dataset from CSV file
def load_books_from_csv(filename):
    books = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Accepts columns named 'title' and 'author' (case-insensitive)
        for row in reader:
            # Try to find the correct keys regardless of case
            title = row.get('title') or row.get('Title') or ''
            author = row.get('author') or row.get('Author') or ''
            books.append({'title': title, 'author': author})
    return books
# Linear search: returns all books where keyword is in title or author (case-insensitive)
def linear_search(books, keyword):
    keyword = keyword.lower()
    results = []
    for book in books:
        if keyword in book['title'].lower() or keyword in book['author'].lower():
            results.append(book)
    return results
# Binary search helpers
def binary_search_books(sorted_books, keyword, key='title'):
    # Returns all books where keyword is in the key field (case-insensitive, partial match)
    keyword = keyword.lower()
    results = []
    n = len(sorted_books)
    left, right = 0, n - 1
    found_indices = set()
    # Binary search to find one occurrence
    while left <= right:
        mid = (left + right) // 2
        field = sorted_books[mid][key].lower()
        if keyword in field:
            found_indices.add(mid)
            # Expand to find all matches around mid
            # Search left
            l = mid - 1
            while l >= 0 and keyword in sorted_books[l][key].lower():
                found_indices.add(l)
                l -= 1
            # Search right
            r = mid + 1
            while r < n and keyword in sorted_books[r][key].lower():
                found_indices.add(r)
                r += 1
            break
        elif keyword < field:
            right = mid - 1
        else:
            left = mid + 1
    # Collect results
    for idx in sorted(found_indices):
        results.append(sorted_books[idx])
    return results
# Hash-based search: build hash table for fast lookup (exact and partial match)
def build_hash_table(books, key='title'):
    hash_table = {}
    for book in books:
        field = book[key].lower()
        if field not in hash_table:
            hash_table[field] = []
        hash_table[field].append(book)
    return hash_table
def hash_search(hash_table, keyword):
    keyword = keyword.lower()
    results = []
    # Exact match
    if keyword in hash_table:
        results.extend(hash_table[keyword])
    # Partial match (slower, but still faster than linear for large datasets)
    for field in hash_table:
        if keyword in field and field != keyword:
            results.extend(hash_table[field])
    return results
def print_results(results):
    if not results:
        print("No matching entries found.")
    else:
        for idx, book in enumerate(results, 1):
            print(f"{idx}. Title: {book['title']}, Author: {book['author']}")
def main():
    # Use the provided CSV file path
    filename = r"C:\Users\Sumalatha\OneDrive\Desktop\AIAC\lab12\ai assisted coding.csv"
    try:
        books = load_books_from_csv(filename)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    if not books:
        print("No books loaded.")
        return
    print(f"Loaded {len(books)} books.")
    keyword = input("Enter a keyword to search (in title or author): ").strip()
    if not keyword:
        print("No keyword entered.")
        return
    # Linear Search
    start = time.time()
    linear_results = linear_search(books, keyword)
    linear_time = time.time() - start
    print(f"\nLinear Search found {len(linear_results)} results in {linear_time:.6f} seconds.")
    # Binary Search (on title)
    sorted_books = sorted(books, key=lambda x: x['title'].lower())
    start = time.time()
    binary_results = binary_search_books(sorted_books, keyword, key='title')
    binary_time = time.time() - start
    print(f"Binary Search (title) found {len(binary_results)} results in {binary_time:.6f} seconds.")
    # Hash-based Search (on title)
    hash_table = build_hash_table(books, key='title')
    start = time.time()
    hash_results = hash_search(hash_table, keyword)
    hash_time = time.time() - start
    print(f"Hash-based Search (title) found {len(hash_results)} results in {hash_time:.6f} seconds.")
    print("\nSample Results (from Linear Search):")
    print_results(linear_results[:10])
    print("\nEfficiency Comparison:")
    print(f"Linear Search Time: {linear_time:.6f} seconds")
    print(f"Binary Search Time: {binary_time:.6f} seconds")
    print(f"Hash-based Search Time: {hash_time:.6f} seconds")
if __name__ == "__main__":
    main()