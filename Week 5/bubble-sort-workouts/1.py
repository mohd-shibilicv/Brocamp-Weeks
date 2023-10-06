def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = ['apple', 'orange', 'grapes', 'lemon', 'banana']

bubbleSort(arr)

print(arr)