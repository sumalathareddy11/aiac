import random
import time

def generate_students(n):
    return [(f"Student_{i+1}", f"R{1000+i}", round(random.uniform(5.0, 10.0), 2)) for i in range(n)]

def quick_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    if reverse:
        left = [x for x in arr if key(x) > key(pivot)]
        mid = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) < key(pivot)]
    else:
        left = [x for x in arr if key(x) < key(pivot)]
        mid = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) > key(pivot)]
    return quick_sort(left, key, reverse) + mid + quick_sort(right, key, reverse)

def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    return merge(merge_sort(arr[:mid], key, reverse), merge_sort(arr[mid:], key, reverse), key, reverse)

def merge(left, right, key, reverse):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (key(left[i]) > key(right[j])) if reverse else (key(left[i]) < key(right[j])):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def print_top_10(students):
    print("Top 10 Students by CGPA:")
    print("{:<15} {:<10} {:<5}".format("Name", "Roll No", "CGPA"))
    for s in students[:10]:
        print("{:<15} {:<10} {:<5}".format(s[0], s[1], s[2]))

if __name__ == "__main__":
    n = 100000
    students = generate_students(n)
    t0 = time.time()
    sorted_quick = quick_sort(students, key=lambda x: x[2], reverse=True)
    print(f"Quick Sort Time: {time.time()-t0:.4f} seconds")
    t0 = time.time()
    sorted_merge = merge_sort(students, key=lambda x: x[2], reverse=True)
    print(f"Merge Sort Time: {time.time()-t0:.4f} seconds")
    print_top_10(sorted_quick)