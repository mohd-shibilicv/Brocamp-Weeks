def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quickSort(lesser) + [pivot] + quickSort(greater)


arr = [30, 10, 3, 50, 20]
print(quickSort(arr))
