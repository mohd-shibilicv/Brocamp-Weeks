class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]
    
    def displayStack(self):
        for item in self.items:
            print(item)

stack = Stack()

stack.push(100)
stack.push(200)
stack.push(300)

print("Stack Elements :")
elements = stack.displayStack()

popped_element = stack.pop()
print("Popped Element:", popped_element)
popped_element = stack.pop()
print("Popped Element:", popped_element)
popped_element = stack.pop()
print("Popped Element:", popped_element)
popped_element = stack.pop()
if popped_element == -1:
    print("Stack Underflow")
else:
    print("Popped Element:", popped_element)

top = stack.top()
print("Top Element :", top)

print("Is the Stack Empty ?:", stack.is_empty())
print("Size of the Stack :", stack.size())
