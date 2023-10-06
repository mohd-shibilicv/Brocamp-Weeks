class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key = lambda x: x[1])

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return None
        item, priority = self.queue.pop(0)
        return item
    
    def displayPriorityQueue(self):
        for item in self.queue:
            print(item)
    

priority_queue = PriorityQueue()

priority_queue.enqueue("Task 1", 3)
priority_queue.enqueue("Task 2", 1)
priority_queue.enqueue("Task 3", 2)

priority_queue.displayPriorityQueue()

print("First task executed :", priority_queue.dequeue()) # Outputs : Task 2
print("Second task executed :", priority_queue.dequeue()) # Outputs : Task 3
print("Third task executed :", priority_queue.dequeue()) # Outputs : Task 1
