def bubbleSort(arr):
    size = len(arr)

    for i in range(size):
        for j in range(0, size-i-1):
                if arr[j] > arr[j + 1]:
                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [50, 20, 40, 10, 60]

print(bubbleSort(arr))
