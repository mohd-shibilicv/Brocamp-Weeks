import heapq

def kth_largest_element(nums, k):
    if k < 1 or k > len(nums):
        return None
    
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    kth_largest = None
    for _ in range(k):
        kth_largest = -heapq.heappop(max_heap)

    return kth_largest


nums = [10, 1, 5, 2, 7, 8]
k = 3

print(f"{k}th largest element :", kth_largest_element(nums, k))
