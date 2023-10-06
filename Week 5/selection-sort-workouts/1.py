def selectionSort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = ['apple', 'orange', 'banana', 'grapes', 'lemon']

selectionSort(arr)

print(arr)
