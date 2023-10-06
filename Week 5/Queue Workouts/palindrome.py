class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]

    def displayQueue(self):
        for item in self.queue:
            print(item)


def is_palindrome(string):
    queue = Queue()
    for char in string.lower():
        queue.enqueue(char)

    reversed_string = ""
    while not queue.is_empty():
        reversed_string += queue.dequeue()

    reversed_str = string[::-1]
    return string.lower() == reversed_str


# Test cases
str1 = "avzq"
str2 = "level"

print(is_palindrome(str1))  # Output: False (str1 is not a palindrome)
print(is_palindrome(str2))  # Output: True (str2 is a palindrome)
