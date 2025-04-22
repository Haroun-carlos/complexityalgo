# 📦 Imports
import random
import time
import matplotlib.pyplot as plt

# 📌 Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 📌 Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 📌 Selection Sort
def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 📌 Radix Sort (LSD, base 10)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = i // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in reversed(arr):
        index = i // exp
        output[count[index % 10] - 1] = i
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]
    return arr

def radix_sort(arr):
    arr = arr.copy()
    max_num = max(arr) if arr else 0
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

# 📌 Python Built-in Sort
def builtin_sort(arr):
    return sorted(arr)

# ⏱️ Timing function
def time_function(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

# 🔁 Run benchmarks
def run_benchmarks():
    sizes = [100, 500, 1000, 2000, 5000]
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Radix Sort': radix_sort,
        'Built-in Sort': builtin_sort
    }

    results = {alg: [] for alg in algorithms}

    for size in sizes:
        print(f"\nTesting input size: {size}")
        test_data = [random.randint(1, 999999) for _ in range(size)]

        for name, func in algorithms.items():
            if size > 1000 and name in ['Bubble Sort', 'Insertion Sort', 'Selection Sort']:
                results[name].append(None)  # Too slow to test on large data
                continue
            t = time_function(func, test_data)
            print(f"{name:>15}: {t:.4f} sec")
            results[name].append(t)

    return sizes, results

# 📈 Plotting results
def plot_results(sizes, results):
    plt.figure(figsize=(12, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)
    plt.title("Sorting Algorithm Performance Comparison")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ▶️ Run Everything
sizes, results = run_benchmarks()
plot_results(sizes, results)
