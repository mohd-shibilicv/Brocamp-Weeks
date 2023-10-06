class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]
        
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        
    def displayQueue(self):
        for item in self.items:
            print(item)
        

queue = Queue()

queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(500)

print("Queue Elements :")
queue.displayQueue()

print("Size of the Queue :", queue.size())

print("Is the Queue empty ? ", queue.is_empty())

print("Front of the Queue :", queue.front())

print("Rear of the Queue :", queue.rear())

print("Popped element :", queue.dequeue())
