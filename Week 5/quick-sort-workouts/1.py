def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)


arr = ['apple', 'lemon', 'banana', 'grapes', 'orange']

quickSort(arr)

print(arr)
