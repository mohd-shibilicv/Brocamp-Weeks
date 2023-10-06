import time
import random

def heapify(arr, n, i):
    largest = i
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    if left_child_index < n and arr[left_child_index] > arr[largest]:
        largest = left_child_index

    if right_child_index < n and arr[right_child_index] > arr[largest]:
        largest = right_child_index

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    # Implement Heap Sort here
    n = len(arr)

    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def quick_sort(arr):
    # Implement Quick Sort here
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    # Implement Merge Sort here
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def measure_time(sort_function, input_size):
    data = [random.randint(1, 1000000) for _ in range(input_size)]
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time


input_sizes = [100, 1000, 5000, 10000]

for size in input_sizes:
    heap_time = measure_time(heap_sort, size)
    quick_time = measure_time(quick_sort, size)
    merge_time = measure_time(merge_sort, size)

    print(f"Input Size: {size}")
    print(f"Heap Sort Time: {heap_time:.6f} seconds")
    print(f"Quick Sort Time: {quick_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print()
