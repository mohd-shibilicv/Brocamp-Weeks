class MinHeap:
    def __init__(self):
        self.heap = []

    def build(self, list_elements):
        self.heap = list_elements[:]

        for i in range(len(self.heap) // 2, -1, -1):
            self._heapify_down(i)

    def push(self, item):
        self.heap.append(item)
        self._heapify_up()

    def _heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return min_element

    def _heapify_down(self, index=0):        
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def display(self):
        levels = self._calculate_levels()

        for level in range(levels):
            print("Level", level, ": ", end="")
            for i in range(2 ** level - 1, min(2 ** (level + 1) - 1, len(self.heap))):
                print(self.heap[i], end=" ")
            print()

    def _calculate_levels(self):
        return len(bin(len(self.heap))) - 2


min_heap = MinHeap()

elements = [21,1,45,78,3,5]
min_heap.build(elements)

min_heap.push(100)
min_heap.push(8)
min_heap.push(3)
min_heap.push(50)

print(min_heap.pop())
print(min_heap.pop())

min_heap.display()
