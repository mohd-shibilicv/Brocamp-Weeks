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
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [20, 30, 5, 21, 42, 90, 64]

heap_sort(arr)

print(arr)
