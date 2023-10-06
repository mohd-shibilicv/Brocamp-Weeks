class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            popped_element = self.head.data
            self.head = self.head.next
            return popped_element
        else:
            print("Underflow")
            return
        
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("Underflow")
            return
        
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next

        return count
    
    def displayStack(self):
        if not self.is_empty():
            current_node = self.head
            while current_node:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")
        else:
            print("Underflow")
            return
    

stack = Stack()

stack.push(100)
stack.push(200)
stack.push(300)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.size())

print(stack.is_empty())

stack.displayStack()
