import random
import time
import matplotlib.pyplot as plt

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search (requires sorted input)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Sizes to test
sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]

# Dictionaries to store timing results
results_existing = {'Linear': [], 'Binary': [], 'In': []}
results_non_existing = {'Linear': [], 'Binary': [], 'In': []}

for size in sizes:
    data = random.sample(range(size * 10), size)
    sorted_data = sorted(data)

    # Existing element
    target_exist = random.choice(data)

    # Non-existing element
    target_non_exist = size * 10 + 1

    # --- Existing ---
    start = time.perf_counter()
    linear_search(data, target_exist)
    results_existing['Linear'].append(time.perf_counter() - start)

    start = time.perf_counter()
    binary_search(sorted_data, target_exist)
    results_existing['Binary'].append(time.perf_counter() - start)

    start = time.perf_counter()
    target_exist in sorted_data
    results_existing['In'].append(time.perf_counter() - start)

    # --- Non-Existing ---
    start = time.perf_counter()
    linear_search(data, target_non_exist)
    results_non_existing['Linear'].append(time.perf_counter() - start)

    start = time.perf_counter()
    binary_search(sorted_data, target_non_exist)
    results_non_existing['Binary'].append(time.perf_counter() - start)

    start = time.perf_counter()
    target_non_exist in sorted_data
    results_non_existing['In'].append(time.perf_counter() - start)
plt.figure(figsize=(10, 6))
plt.plot(sizes, results_existing['Linear'], label='Linear Search', marker='o')
plt.plot(sizes, results_existing['Binary'], label='Binary Search', marker='s')
plt.plot(sizes, results_existing['In'], label='Python in operator', marker='^')
plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.title("Search Time for Existing Elements")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(12, 6))

# Linear Search
plt.plot(sizes, results_existing['Linear'], label='Linear (Exists)', linestyle='-')
plt.plot(sizes, results_non_existing['Linear'], label='Linear (Not Exists)', linestyle='--')

# Binary Search
plt.plot(sizes, results_existing['Binary'], label='Binary (Exists)', linestyle='-')
plt.plot(sizes, results_non_existing['Binary'], label='Binary (Not Exists)', linestyle='--')

# In operator
plt.plot(sizes, results_existing['In'], label='In (Exists)', linestyle='-')
plt.plot(sizes, results_non_existing['In'], label='In (Not Exists)', linestyle='--')

plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.title("Comparison: Existing vs Non-Existing Element Search Time")
plt.legend()
plt.grid(True)
plt.show()
