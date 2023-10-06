class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Underflow")
            return
        popped_element = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped_element

    def fronts(self):
        if self.is_empty():
            print("Underflow")
            return
        return self.front.data

    def rears(self):
        if self.is_empty():
            print("Underflow")
            return
        return self.rear.data    
        
    def size(self):
        count = 0
        current_node = self.front
        while current_node:
            count += 1
            current_node = current_node.next
        return count

        
    def displayQueue(self):
        if not self.is_empty():
            current_node = self.front
            while current_node:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")
        else:
            print("Underflow")
            return
        

queue = Queue()

queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)

print(queue.dequeue())

print(queue.size())

print(queue.fronts())
print(queue.rears())

print(queue.is_empty())

queue.displayQueue()
