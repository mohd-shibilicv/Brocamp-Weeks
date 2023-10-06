class MaxHeap:
    def __init__(self):
        self.heap = []

    def build(self, elements):
        self.heap = elements[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self._heapify_down(i)

    def push(self, item):
        self.heap.append(item)
        self._heapify_up()

    def _heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return min_item

    def _heapify_down(self, index=0):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            greatest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[greatest]:
                greatest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[greatest]:
                greatest = right_child_index

            if greatest == index:
                break

            self.heap[index], self.heap[greatest] = self.heap[greatest], self.heap[index]
            index = greatest

    def display(self):
        levels = self._calculate_levels()
        for level in range(levels):
            print("Level", level, ": ", end="")
            for i in range(2 ** level - 1, min(2 ** (level + 1) - 1, len(self.heap))):
                print(self.heap[i], end=" ")
            print()

    def _calculate_levels(self):
        return len(bin(len(self.heap))) - 2


max_heap = MaxHeap()

list = [2, 5, 12, 34, 3]
max_heap.build(list)

max_heap.push(50)
max_heap.push(1)

max_heap.pop()

max_heap.display()
