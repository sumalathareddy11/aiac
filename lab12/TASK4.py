import random
import time

def simulate_stock_data(n):
    stocks = []
    for i in range(n):
        o = round(random.uniform(10, 500), 2)
        c = round(o * (1 + random.uniform(-0.15, 0.15)), 2)
        stocks.append({
            'symbol': f"STK{i+1:03d}",
            'open': o,
            'close': c,
            'pct_change': (c - o) / o * 100
        })
    return stocks

def heapify(arr, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and key(arr[l]) > key(arr[largest]):
        largest = l
    if r < n and key(arr[r]) > key(arr[largest]):
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key=lambda x: x):
    arr = arr.copy()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key)
    arr.reverse()
    return arr

def build_stock_hash(stocks):
    return {s['symbol']: s for s in stocks}

def search_stock(stock_hash, symbol):
    return stock_hash.get(symbol)

def print_top_stocks(stocks, n=10):
    print(f"{'Symbol':<8} {'Open':>10} {'Close':>10} {'% Change':>10}")
    print('-' * 40)
    for s in stocks[:n]:
        print(f"{s['symbol']:<8} {s['open']:>10.2f} {s['close']:>10.2f} {s['pct_change']:>10.2f}")

def main():
    n_stocks = 10000
    random.seed(123)
    stocks = simulate_stock_data(n_stocks)

    t = time.time()
    sorted_heap = heap_sort(stocks, key=lambda x: x['pct_change'])
    heap_time = time.time() - t

    t = time.time()
    sorted_std = sorted(stocks, key=lambda x: x['pct_change'], reverse=True)
    std_time = time.time() - t

    print("Top 10 Stocks by % Change (Heap Sort):")
    print_top_stocks(sorted_heap, 10)
    print("\nTop 10 Stocks by % Change (sorted()):")
    print_top_stocks(sorted_std, 10)
    print(f"\nHeap Sort Time: {heap_time:.6f} s\nsorted() Time: {std_time:.6f} s")

    t = time.time()
    stock_hash = build_stock_hash(stocks)
    hash_build_time = time.time() - t

    test_symbol = stocks[n_stocks // 2]['symbol']

    t = time.time()
    found = search_stock(stock_hash, test_symbol)
    hash_lookup_time = time.time() - t

    t = time.time()
    found_linear = next((s for s in stocks if s['symbol'] == test_symbol), None)
    linear_search_time = time.time() - t

    print(f"\nHash Map Build: {hash_build_time:.6f} s\nDict Lookup: {hash_lookup_time:.8f} s\nLinear Search: {linear_search_time:.8f} s\nSample ({test_symbol}): {found}")
    print("\nTrade-offs:\n- Heap Sort O(n log n); sorted() (Timsort) is highly optimized and usually faster.\n- Dict lookup ~O(1) avg; linear search O(n). Dict uses extra memory but enables instant retrieval.")

    while True:
        symbol = input("\nEnter stock symbol to search (or 'exit'): ").strip().upper()
        if symbol == 'EXIT':
            break
        r = search_stock(stock_hash, symbol)
        if r:
            print(f"Symbol: {r['symbol']}, Open: {r['open']:.2f}, Close: {r['close']:.2f}, % Change: {r['pct_change']:.2f}")
        else:
            print("Stock symbol not found.")

if __name__ == "__main__":
    main()